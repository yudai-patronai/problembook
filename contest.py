#!/usr/bin/python3

import argparse
import os
import sys
import traceback
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


class ProblemValidationError(Exception):
    def __init__(self, errors):
        super(ProblemValidationError, self).__init__()
        self.errors = errors


class Problem:

    def __init__(self, ppath):
        self._prob = frontmatter.load(ppath)

        self.path = os.path.dirname(ppath)
        self.tests_dir = os.path.join(self.path, TESTS_FOLDER)
        self.generator = os.path.abspath(os.path.join(self.path, TEST_GENERATOR))

        self.statement = ppath
        self.metadata = self._prob.metadata
        self.content = self._prob.content

        errors = []
        if 'id' not in self.metadata:
            errors.append('{}: не указан id'.format(self.statement))
        if 'longname' not in self.metadata:
            errors.append('{}: не указан longname' .format(self.statement))

        if errors:
            raise ProblemValidationError(errors)

        if 'tags' not in self.metadata:
            self.metadata['tags'] = []

    def __getattr__(self, item):
        return self.metadata[item]

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__ = d

    def has_tests(self):
        return os.path.isdir(self.tests_dir)

    def has_solution(self):
        return os.path.isfile(os.path.join(self.path, 'solution.py'))

    def has_test_generator(self):
        return os.path.isfile(os.path.join(self.path, 'test_generator.py'))

    def generate_tests(self):
        subprocess.check_output([sys.executable, self.generator], cwd=self.path)

    def validate(self):
        errors = []

        if 'checker' not in self.metadata:
            if not os.path.isfile(os.path.join(self.path, 'checker.py')):
                errors.append('{}: чекер не найден'.format(self.path))
        else:
            c = self.metadata['checker']
            if c.startswith('cmp'):
                if c not in ['cmp_yesno', 'cmp_int', 'cmp_int_seq', 'cmp_file']:
                    errors.append('{}: неизвестный чекер'.format(self.path))

        if not self.has_tests():
            errors.append('{}: тесты не сгенерированы'.format(self.path))

        if not self.has_solution():
            errors.append('{}: отсутствует решение'.format(self.path))

        if not self.has_test_generator():
            errors.append('{}: отсутствует генератор тестов'.format(self.path))

        if errors:
            raise ProblemValidationError(errors)


def parse_io_example(block):
    lines = [l.strip() for l in block.split('\n')]

    _in = []
    _out = []

    flag = 0

    if len(lines) < 3:
        return None

    if lines[0] == lines[-1] == '```':
        lines = lines[1:-1]

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
        table.set('class', 'example')
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

    problems = __find_problems(lambda p: p.id in requested)

    diff = requested.difference(problems.keys())
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
        f.write(template.render(name=params.name, problems=[problems[k] for k in params.problems]))


def find_problems(params):
    problems = [[
        k+1,
        p.id,
        p.longname,
        ' '.join(p.tags)
    ] for k, p in enumerate(__find_problems().values())]

    print(tabulate.tabulate(
        problems,
        headers=['#', 'Идентификатор', 'Название', 'Теги']
    ))


def __find_problems(predicate=None):

    problems = {}

    for root, _, files in os.walk(PROBLEMS_DIR):
        for file in files:
            fname, fext = os.path.splitext(file.lower())
            if fname == 'statement' and fext[1:] in ALLOWED_MD_LANGS:
                ppath = os.path.join(root, file)
                try:
                    problem = Problem(ppath)
                except ProblemValidationError as e:
                    print(*e.errors, sep='\n')
                    continue
                except:
                    print('Ошибка при загрузке условия: {}'.format(ppath))
                    if args.verbose:
                        traceback.print_exc()
                    continue

                if predicate and not predicate(problem):
                    continue

                problems[problem.id] = problem

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

    ids = [list(p.keys())[0] for p in desc['problems']]
    ids_set = set(ids)
    problems_dict = __find_problems(lambda p: p.id in ids_set)

    found = True
    for k in ids_set:
        if k not in problems_dict:
            print('{}: задача не найдена'.format(k))
            found = False
    if not found:
        sys.exit(-1)

    for k, p in enumerate(ids):
        problems_dict[p].metadata['shortname'] = chr(ord('A') + k)
        problems_dict[p].metadata.update(problem_overrides.get(problems_dict[p].metadata['id']))

    problems = [problems_dict[p] for p in ids]

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
            shutil.copy(os.path.join(p.path, 'checker.py'), problem_dir)
        shutil.copytree(p.tests_dir, os.path.join(problem_dir, TESTS_FOLDER))


def generate_tests_for_problem(prob, force=False):
    if prob.has_tests() and not force:
        print('Пропускаю генерацию тестов для ' + prob.path)
        return

    print('Генерирую тесты для ' + prob.path)

    try:
        prob.generate_tests()
    except subprocess.CalledProcessError as e:
        print("Ошибка при генерации тестов для {}: {}".format(prob.path, e.output))


def generate_tests(params):

    with multiprocessing.Pool(params.jobs) as p:
        p.map(functools.partial(generate_tests_for_problem, force=params.force_overwrite), __find_problems().values())


def validate(params):
    problems = __find_problems().values()

    ids = set()

    for p in problems:
        try:
            p.validate()
        except ProblemValidationError as e:
            print(*e.errors, sep='\n')

            if p.id in ids:
                print('{}: не уникальный id'.format(p.path))
            else:
                ids.add(p.id)


def show(params):
    prob = next(iter(__find_problems(lambda p: p.id == params.id).values()))

    with open(prob.statement) as f:
        print(f.read())


def edit(params):
    problem = next(iter(__find_problems(lambda p: p.id == params.id).values()))
    editor = subprocess.check_output(['which', os.environ.get('EDITOR', 'vim')]).decode('utf-8').strip()
    os.execl(editor, editor, problem.statement)

parser = argparse.ArgumentParser(prog='contest')
parser.add_argument('-v', '--verbose', action='store_true', help='Включить подробный вывод')
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

edit_parser = subparsers.add_parser('edit', help='Отредактировать описание задачи')
edit_parser.set_defaults(_action=edit)
edit_parser.add_argument('id', help='Идентификатор задачи')

args = parser.parse_args()

args._action(args)