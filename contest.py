#!/usr/bin/python3

import argparse
import os
import sys
import functools
import multiprocessing
import subprocess
import shutil
import uuid
import lxml.etree
import jinja2
import frontmatter
import tabulate
import yaml
import markdown
import html2markdown
import bs4

#ALLOWED_MD_LANGS = ['md', 'rst']
ALLOWED_MD_LANGS = ['md']
SCRIPT_DIR = os.path.dirname(__file__)
PROBLEMS_DIR = os.path.join(SCRIPT_DIR, 'problems')
CONTESTS_DIR = os.path.join(SCRIPT_DIR, 'contests')
TESTS_FOLDER = 'tests'
TEST_GENERATOR = 'test_generator.py'

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(SCRIPT_DIR, 'templates')),
)


def parse_io_example(block):
    lines = [l.strip() for l in block.split('\n')]

    _in = []
    _out = []

    flag = 0

    for l in lines:
        if flag == 0:
            if l.startswith('-> '):
                _in.append(l[3:])
            elif l == '--':
                flag = 1
            else:
                return None
        else:
            if l.startswith('<- '):
                _out.append(l[3:])
            else:
                return None

    return _in, _out


class InputOutputExamplesProcessor(markdown.blockprocessors.BlockProcessor):

    def test(self, parent, block):
        return parse_io_example(block) is not None

    def run(self, parent, blocks):
        example = parse_io_example(blocks.pop(0))

        etree = markdown.util.etree

        table = etree.SubElement(parent, 'table')
        thead = etree.SubElement(table, 'thead')
        tr = etree.SubElement(thead, 'tr')

        for el in ['Ввод', 'Вывод']:
            etree.SubElement(tr, 'td').text = el

        tbody = etree.SubElement(table, 'tbody')
        tr = etree.SubElement(tbody, 'tr')

        for el in example:
            td = etree.SubElement(tr, 'td')
            etree.SubElement(td, 'pre').text = '\n'.join(el)

        etree.SubElement(parent, 'br')


class InputOutputExamplesExtension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        md.parser.blockprocessors.add('ioexample', InputOutputExamplesProcessor(md.parser), '>indent')


def create_problem(params):
    _params = params.__dict__.copy()

    if _params['from_xml']:
        xml = lxml.etree.parse(_params['from_xml'])
        if 'longname' not in params:
            params['longname'] = xml.xpath('/problem/statement/title/text()')[0].strip()

        _params['content'] = {'examples': []}

        desc = xml.xpath('/problem/statement/description')[0]
        html = (desc.text or '') + ''.join(lxml.etree.tostring(x).decode('utf-8') for x in desc.getchildren()) + (desc.tail or '')
        _params['content']['description'] = html2markdown.convert(html)

        for ex in xml.xpath('/problem/examples/example'):
            _in = [l.strip() for l in ex.xpath('input/text()')[0].split('\n') if l]
            _out = [l.strip() for l in ex.xpath('output/text()')[0].split('\n') if l]
            _params['content']['examples'].append((_in, _out))

    lng = params.markdown_language

    template = env.get_template('problem.{}.jinja2'.format(lng))

    problem_dir = os.path.join(PROBLEMS_DIR, params.path)
    os.makedirs(problem_dir, exist_ok=True)

    with open(os.path.join(problem_dir, 'statement.' + lng), 'w') as f:
        f.write(template.render(id=str(uuid.uuid4()), **_params))


def create_contest(params):
    os.makedirs(CONTESTS_DIR, exist_ok=True)

    requested = set(params.problems)

    problems = __find_problems(lambda p: p.metadata['id'] in requested)

    found = set(p.metadata['id'] for p in problems)

    diff = requested.difference(found)
    if diff:
        for p in diff:
            print('Задача не найдена:', p)
        sys.exit(1)

    contest_file = os.path.join(CONTESTS_DIR, "{}.yml".format(params.name))
    if os.path.isfile(contest_file) and not params.force_overwrite:
        sys.stderr.write('Файл {} уже существует'.format(contest_file))
        sys.exit(-1)

    template = env.get_template('contest.yml.jinja2')
    with open(contest_file, 'w') as f:
        f.write(template.render(name=params.name, problems=problems))


def find_problems(params):
    problems = [[
        k,
        p.metadata['id'],
        p.metadata['longname'],
        ' '.join(p.metadata['tags'])
    ] for k, p in enumerate(__find_problems())]

    print(tabulate.tabulate(
        problems,
        headers=['#', 'Идентификатор', 'Название', 'Теги']
    ))


def __find_problems(predicate=None):

    problems = []

    k = 1
    for root, _, files in os.walk(PROBLEMS_DIR):
        for file in files:
            fname, fext = os.path.splitext(file.lower())
            if fname == 'statement' and fext[1:] in ALLOWED_MD_LANGS:
                ppath = os.path.join(root, file)
                problem = frontmatter.load(ppath)
                problem.metadata['path'] = os.path.dirname(ppath)
                problem.metadata['statement'] = ppath
                if predicate and not predicate(problem):
                    continue
                problems.append(problem)
                k += 1

    return problems


def generate_ejudge_config(params):
    with open(params.contest) as f:
        desc = yaml.load(f)

    problem_overrides = dict(next(iter(p.items())) for p in desc['problems'])

    root_dir = os.path.join(params.output_dir, str(desc['name']))
    if os.path.isdir(root_dir):
        if not params.force_overwrite:
            sys.stderr.write('Директория {} уже существует.'.format(root_dir))
            sys.exit(-1)
        else:
            shutil.rmtree(root_dir)

    conf_dir = os.path.join(root_dir, 'conf')
    problems_dir = os.path.join(root_dir, 'problems')
    statements_dir = os.path.join(root_dir, 'statements')

    os.makedirs(conf_dir, exist_ok=True)
    os.makedirs(problems_dir, exist_ok=True)
    os.makedirs(statements_dir, exist_ok=True)

    ids = set(list(p.keys())[0] for p in desc['problems'])
    problems = __find_problems(lambda p: p['id'] in ids)
    for k, p in enumerate(problems):
        p.metadata['shortname'] = chr(ord('A') + k)
        p.metadata.update(problem_overrides.get(p.metadata['id']))

    template = env.get_template(params.template)

    with open(os.path.join(conf_dir, 'serve.cfg'), 'w') as f:
        f.write(template.render(problems=map(lambda p: p.metadata, problems)))

    md = markdown.Markdown(extensions = ['markdown.extensions.tables', InputOutputExamplesExtension()])
    for p in problems:
        problem_dir = os.path.join(problems_dir, p.metadata['shortname'])
        os.makedirs(problem_dir, exist_ok=True)
        with open(os.path.join(statements_dir, p.metadata['shortname'] + ".html"), 'w') as f:
            html = md.convert(p.content)
            f.write(bs4.BeautifulSoup(html, 'lxml').prettify())
        generate_tests_for_problem(p)
        if 'checker' not in p.metadata:
            shutil.copy(os.path.join(p.metadata['path'], 'checker.py'), problem_dir)
        shutil.copytree(os.path.join(p.metadata['path'], TESTS_FOLDER), os.path.join(problem_dir, TESTS_FOLDER))


def generate_tests_for_problem(prob, force=False):
    path = os.path.abspath(prob if isinstance(prob, str) else prob.metadata['path'])

    tests_dir = os.path.join(path, TESTS_FOLDER)
    generator = os.path.abspath(os.path.join(path, TEST_GENERATOR))
    if os.path.isdir(tests_dir) and not force:
        print('Пропускаю генерацию тестов для ' + path)
        return

    print('Генерирую тесты для ' + path)

    try:
        subprocess.check_output([sys.executable, generator], cwd=path)
    except subprocess.CalledProcessError as e:
        print("Ошибка при генерации тестов для {}: {}".format(path, e.output))


def generate_tests(params):

    with multiprocessing.Pool(params.jobs) as p:
        p.map(functools.partial(generate_tests_for_problem, force=params.force_overwrite), __find_problems())


def validate(params):
    problems = __find_problems()

    ids = set()

    for p in problems:
        path = p.metadata['path']
        if 'id' not in p.metadata:
            print('{}: не указан id'.format(path))
        else:
            if p.metadata['id'] in ids:
                print('{}: не уникальный id'.format(path))
            else:
                ids.add(p.metadata['id'])

        if 'longname' not in p.metadata:
            print('{}: не указано название задачи'.format(path))

        if 'checker' not in p.metadata:
            if not os.path.isfile(os.path.join(path, 'checker.py')):
                print('{}: чекер не найден'.format(path))
        else:
            c = p.metadata['checker']
            if c.startswith('cmp'):
                if c not in ['cmp_yesno', 'cmp_int', 'cmp_int_seq']:
                    print('{}: неизвестный чекер'.format(path))

        if not os.path.isdir(os.path.join(path, 'tests')):
            print('{}: тесты не сгенерированы'.format(path))

        if not os.path.isfile(os.path.join(path, 'solution.py')):
            print('{}: отсутствует решение'.format(path))

        if not os.path.isfile(os.path.join(path, 'test_generator.py')):
            print('{}: отсутствует генератор тестов'.format(path))


def show(params):
    prob = __find_problems(lambda p: p.metadata['id'] == params.id)[0]

    with open(prob.metadata['statement']) as f:
        print(f.read())

parser = argparse.ArgumentParser(prog='contest')
subparsers = parser.add_subparsers(dest='cmd')
subparsers.required = True

create_problem_parser = subparsers.add_parser('create-problem', help='Создать задачу')
create_problem_parser.set_defaults(_action=create_problem)
create_problem_parser.add_argument('-p', '--path', required=True, help='Путь, по которому будет создана задача')
create_problem_parser.add_argument('-t', '--tags', default='', help='Список тегов через запятую')
create_problem_parser.add_argument('-L', '--markdown-language', default=ALLOWED_MD_LANGS[0], choices=ALLOWED_MD_LANGS, help='Язык разметки')
create_problem_parser.add_argument('-l', '--longname', help='Длинное название')
create_problem_parser.add_argument('-F', '--from-xml', help='Описание в задачи в xml для импорта')

create_contest_parser = subparsers.add_parser('create-contest', help='Создать контест')
create_contest_parser.set_defaults(_action=create_contest)
create_contest_parser.add_argument('-n', '--name', required=True, help='Название контеста')
create_contest_parser.add_argument('-f', '--force-overwrite', action='store_true', help='Перезаписывать существующие конфиги контестов')
create_contest_parser.add_argument('problems', nargs='+', help='Список идентификаторов задач')

find_problems_parser = subparsers.add_parser('find-problems', help='Найти задачи')
find_problems_parser.set_defaults(_action=find_problems)

generate_ejudge_config_parser = subparsers.add_parser('ejudge', help='Сгенерировать конфиг ejudge')
generate_ejudge_config_parser.set_defaults(_action=generate_ejudge_config)
generate_ejudge_config_parser.add_argument('contest', help='Файл с описание контеста')
generate_ejudge_config_parser.add_argument('-t', '--template', required=True, help='Шаблон конфига')
generate_ejudge_config_parser.add_argument('-o', '--output-dir', required=True, help='Выходной путь')
generate_ejudge_config_parser.add_argument('-f', '--force-overwrite', action='store_true', help='Перезаписывать существующие конфиги ejudge')

generate_tests_parser = subparsers.add_parser('generate-tests', help='Сгенерировать тесты')
generate_tests_parser.set_defaults(_action=generate_tests)
generate_tests_parser.add_argument('-j', '--jobs', default=1, type=int, help='Количество параллельных потоков для генерации')
generate_tests_parser.add_argument('-f', '--force-overwrite', action='store_true', help='Перезаписывать существующие тесты')

validate_parser = subparsers.add_parser('validate', help='Проверить корректность условий в репозитории')
validate_parser.set_defaults(_action=validate)

show_parser = subparsers.add_parser('show', help='Показать описание задачи')
show_parser.set_defaults(_action=show)
show_parser.add_argument('id', help='Идентификатор задачи')


args = parser.parse_args()

args._action(args)
