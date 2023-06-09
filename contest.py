#!/usr/bin/env python3

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
import tempfile
import hashlib
import time
from termcolor import colored
import github3
import getpass
import pickle

import lib.problembook as pb
import lib.problembook.git as git


#ALLOWED_MD_LANGS = ['md', 'rst']
ALLOWED_MD_LANGS = ['md']
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROBLEMS_DIR = os.path.join(SCRIPT_DIR, 'problems')
CONTESTS_DIR = os.path.join(SCRIPT_DIR, 'contests')
CACHE_FILE = os.path.join(SCRIPT_DIR, '.cache')
TESTS_FOLDER = 'tests'
TEST_GENERATOR = 'test_generator.py'
CHECKSUM = 'checksum'
CHECKER = 'checker.py'
HEADER = 'header'
FOOTER = 'footer'
SOLUTION = 'solution'

EXTENSION_MAP = {
    'cpp': '.cpp',
    'c': '.c',
    'python': '.py'
}

LINT_MAP = {
    'cpp': ['cclint', '--filter=-legal/copyright'],
    'c': ['cclint', '--filter=-legal/copyright'],
    'python': ['pycodestyle']
}

CPP_COMPILER = 'g++'
CPP_FLAGS = ['-std=c++11', '-Wall', '-Wextra', '-Wpedantic', '-Werror']

MARK_UNKNOWN = "?"
MARK_OK = colored('✓', 'green')
MARK_FAILED = colored('✕', 'red')

CREDENTIALS_FILE = os.path.join(SCRIPT_DIR, '.github-token')
ISSUE_BODY = '''\
id: {{ id }}
Путь: {{ path }}

[Описание задачи](https://github.com/mipt-cs/problembook/tree/master/{{ path }})

- [ ] Проверить условие
{% for lang in langs -%}
- [ ] Проверить решение {{ lang }}
{% endfor -%}
{% for lang in missed_langs -%}
- [ ] Написать решение {{ lang }}
{% endfor -%}
- [ ] Проверить генератор тестов
{% if has_checker -%}
- [ ] Проверить чекер
{% endif -%}
- [ ] Добавить/обновить контрольные суммы
'''

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(SCRIPT_DIR, 'templates')),
)
env.filters['basename'] = os.path.basename

class Problem:

    ERROR_ID_MISSING = 0
    ERROR_LONGNAME_MISSING = 1
    ERROR_CHECKER_NOT_FOUND = 2
    ERROR_CHECKER_UNKNOWN = 3
    ERROR_TESTS_MISSING = 4
    ERROR_SOLUTION_MISSING = 5
    ERROR_TEST_FAILED = 6
    ERROR_SOLUTION_CANNOT_BE_CHECKED = 7
    ERROR_TEST_GENERATOR_MISSING = 8
    ERROR_CHECKSUM_MISSING = 9
    ERROR_CHECKSUM_MISMATCH = 10
    ERROR_TEST_DUPLICATES = 11
    ERROR_UNKNOWN_LANGUAGE = 12
    ERROR_LANGUAGES_MISSING = 13
    ERROR_SOLUTION_COMPILATION = 14
    ERROR_BAD_CODESTYLE = 15

    ERROR_MESSAGES = {
        ERROR_ID_MISSING: '{0.path}: не указан id',
        ERROR_LONGNAME_MISSING: '{0.path}: не указан longname',
        ERROR_CHECKER_NOT_FOUND: '{0.path}: чекер не найден',
        ERROR_CHECKER_UNKNOWN: '{0.path}: неизвестный чекер',
        ERROR_TESTS_MISSING: '{0.path}: тесты не сгенерированы',
        ERROR_SOLUTION_MISSING: '{0.path}: отсутствует решение для одного или нескольких языков',
        ERROR_TEST_FAILED: '{0.path}: тест {1} не пройден',
        ERROR_SOLUTION_CANNOT_BE_CHECKED: '{0.path}: невозможно проверить решение',
        ERROR_TEST_GENERATOR_MISSING: '{0.path}: отсутствует генератор тестов',
        ERROR_CHECKSUM_MISSING: '{0.path}: отсутствует контрольная сумма',
        ERROR_CHECKSUM_MISMATCH: '{0.path}: контрольные суммы тестов не совпадают',
        ERROR_TEST_DUPLICATES: '{0.path}: совпадают тесты → {1}',
        ERROR_UNKNOWN_LANGUAGE: '{0.path}: неизвестный язык {1}',
        ERROR_LANGUAGES_MISSING: '{0.path}: не указан язык',
        ERROR_SOLUTION_COMPILATION: '{0.path}: ошибка компиляции решения {1}',
        ERROR_BAD_CODESTYLE: '{0.path}: плохой code-style решения {1}'
    }

    def __init__(self, ppath):
        with open(ppath) as f:
            lines = f.readlines()
            for i, l in enumerate(lines):
                if not l.startswith('#'):
                    break
            lines = lines[i:]
        self._prob = frontmatter.loads(''.join(lines))

        self.path = os.path.abspath(os.path.dirname(ppath))
        self.tests_dir = os.path.join(self.path, TESTS_FOLDER)
        self.generator = os.path.abspath(os.path.join(self.path, TEST_GENERATOR))
        self.checksum = os.path.abspath(os.path.join(self.path, CHECKSUM))
        self.author = self.get_first_committer()
        self.last_update = self.get_last_update()

        self.statement = ppath
        self.metadata = self._prob.metadata
        self.content = self._prob.content

        self.errors = []
        if 'id' not in self.metadata:
            self._report_error(Problem.ERROR_ID_MISSING, self.statement)
        if 'longname' not in self.metadata:
            self._report_error(Problem.ERROR_LONGNAME_MISSING, self.statement)
        if 'languages' not in self.metadata:
            self._report_error(Problem.ERROR_LANGUAGES_MISSING, self.statement)

        if 'tags' not in self.metadata:
            self.metadata['tags'] = []
        self.metadata['tags'] = set(self.metadata['tags'])

        if 'languages' not in self.metadata:
            self.metadata['languages'] = []
        self.metadata['languages'] = set(self.metadata['languages'])

    def _report_error(self, error, *args, **kwargs):
        self.errors.append((error, args, kwargs))

    def format_errors(self):
        return '\n'.join(Problem.ERROR_MESSAGES[e].format(self, *args, **kwargs) for e, args, kwargs in self.errors)

    def has_error_occurred(self, e):
        return e in map(lambda x: x[0], self.errors)

    def __getattr__(self, item):
        return self.metadata.get(item, None)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__ = d

    def has_tests(self):
        if not os.path.isdir(self.tests_dir):
            return False

        for l in os.listdir(self.tests_dir):
            if not l.endswith('.a'):
                return True

        return False

    def has_solution(self):
        return all(map(os.path.isfile, [os.path.join(self.path, SOLUTION + EXTENSION_MAP.get(ext, 'NOTFOUND')) for ext in self.languages]))

    def has_test_generator(self):
        return os.path.isfile(os.path.join(self.path, TEST_GENERATOR))

    def has_checksum(self):
        return os.path.isfile(self.checksum)

    def has_checker(self):
        return os.path.isfile(os.path.join(self.path, CHECKER))

    def get_file(self, component, lang):
        path = os.path.join(self.path, component + EXTENSION_MAP[lang])
        return path if os.path.isfile(path) else None

    def get_solution(self, lang):
        return self.get_file(SOLUTION, lang)

    def get_header(self, lang):
        return self.get_file(HEADER, lang)

    def get_footer(self, lang):
        return self.get_file(FOOTER, lang)

    def generate_tests(self):
        subprocess.check_output([sys.executable, self.generator], cwd=self.path, stderr=subprocess.STDOUT)

    def compile_solution_cpp(self, solution_path, output_dir):
        solution_bin = os.path.join(output_dir, os.path.basename(solution_path) + '.bin')
        subprocess.check_call([CPP_COMPILER] + CPP_FLAGS + [solution_path, '-o', solution_bin])

        return solution_bin

    def run_solution_cpp(self, solution_binary, input_path, output_path):
        with open(input_path) as f:
            output = subprocess.check_output([solution_binary], stdin=f).decode()
        with open(output_path, 'w') as f:
            f.write(output)

    def compile_solution_python(self, solution_path, output_dir):
        return solution_path

    def run_solution_python(self, solution_path, input_path, output_path):
        with open(input_path) as f:
            output = subprocess.check_output([sys.executable, solution_path], stdin=f).decode()
        with open(output_path, 'w') as f:
            f.write(output)

    def check_test_output(self, input_file, output_file, answer_file, custom_checker):
        if not custom_checker:
            subprocess.check_call(['diff', '-B', '-w', '-q', output_file, answer_file], cwd=self.path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.check_call([sys.executable, CHECKER, input_file, output_file, answer_file], cwd=self.path, stdout=subprocess.DEVNULL)

    def validate(self, check_checksum=True, check_solution=False, check_codestyle=False):
        self.errors = []

        checker_found = False

        for lang in self.languages:
            if lang not in EXTENSION_MAP:
                self._report_error(Problem.ERROR_UNKNOWN_LANGUAGE, lang)

        if 'checker' not in self.metadata:
            if self.has_checker():
                checker_found = True
            else:
                self._report_error(Problem.ERROR_CHECKER_NOT_FOUND)
        else:
            c = self.metadata['checker']
            if c.startswith('cmp'):
                if c not in ['cmp_yesno', 'cmp_int', 'cmp_int_seq', 'cmp_file', 'cmp_long_long_seq', 'cmp_long_long']:
                    self._report_error(Problem.ERROR_CHECKER_UNKNOWN)

        if not self.has_tests():
            self._report_error(Problem.ERROR_TESTS_MISSING)
        else:
            hashes = {}
            for t in os.listdir(self.tests_dir):
                if not t.endswith('.a'):
                    with open(os.path.join(self.tests_dir, t), 'rb') as f:
                        hash = hashlib.sha512(f.read()).digest()
                        if hash not in hashes:
                            hashes[hash] = [t]
                        else:
                            hashes[hash].append(t)
            duplicates = list(filter(lambda x: len(x) > 1, hashes.values()))
            for d in duplicates:
                self._report_error(Problem.ERROR_TEST_DUPLICATES, ', '.join(d))

        if not self.has_solution():
            self._report_error(Problem.ERROR_SOLUTION_MISSING)

        if check_solution:
            if self.has_tests() and self.has_solution():
                for lang in self.languages:
                    tmp = tempfile.mkdtemp()

                    full_solution = ''
                    delimiter = ''
                    for part in [self.get_header(lang), self.get_solution(lang), self.get_footer(lang)]:
                        if part is None:
                            continue
                        if os.path.isfile(part):
                            with open(part) as f:
                                full_solution += delimiter + f.read()
                                delimiter = '\n\n' # make PEP8 happy

                    full_solution_path = os.path.join(tmp, os.path.basename(self.get_solution(lang)))
                    with open(full_solution_path, 'w') as f:
                        f.write(full_solution)

                    if check_codestyle:
                        try:
                            subprocess.check_call(LINT_MAP[lang] + [full_solution_path])
                        except subprocess.CalledProcessError:
                            self._report_error(Problem.ERROR_BAD_CODESTYLE, self.get_solution(lang))

                    try:
                        binary_solution = getattr(self, 'compile_solution_{}'.format(lang))(full_solution_path, tmp)
                    except subprocess.CalledProcessError:
                        self._report_error(Problem.ERROR_SOLUTION_COMPILATION, self.get_solution(lang))
                        continue

                    tests = list(filter(
                        lambda x: not x.endswith('.a'),
                        map(
                            lambda x: os.path.join(TESTS_FOLDER, x),
                            sorted(os.listdir(self.tests_dir))
                        )
                    ))

                    output_file = os.path.join(tmp, 'output')

                    for t in tests:
                        input_file = os.path.join(self.path, t)

                        try:
                            getattr(self, 'run_solution_{}'.format(lang))(binary_solution, input_file, output_file)
                            self.check_test_output(input_file, output_file, '{}.a'.format(t), checker_found)
                        except subprocess.CalledProcessError:
                            self._report_error(Problem.ERROR_TEST_FAILED, t)

                    shutil.rmtree(tmp)
            else:
                self._report_error(Problem.ERROR_SOLUTION_CANNOT_BE_CHECKED)

        if not self.has_test_generator():
            self._report_error(Problem.ERROR_TEST_GENERATOR_MISSING)

        if check_checksum:
            if not self.has_checksum():
                self._report_error(Problem.ERROR_CHECKSUM_MISSING)
            else:
                try:
                    subprocess.check_call(['sha512sum', '--status', '-c', self.checksum], cwd=self.path)
                except subprocess.CalledProcessError:
                    self._report_error(Problem.ERROR_CHECKSUM_MISMATCH)

    def commit(self):
        tests = list(map(lambda x: os.path.join(TESTS_FOLDER, x), sorted(os.listdir(self.tests_dir))))
        with open(self.checksum, 'w') as output:
            subprocess.check_call(['sha512sum'] + tests, stdout=output, cwd=self.path)

    def mark_fixme(self, value=True):
        if self.fixme and not value:
            add = False
        elif not self.fixme and value:
            add = True
        else:
            return

        with open(self.statement, newline='') as f:
            lines = f.readlines()

        for i, l in enumerate(lines):
            if l.strip() == '---':
                break

        if i == len(lines)-1:
            print('Не могу найти начало метаданных', file=sys.stderr)
            return -1

        if add:
            end = '\r\n' if l[-2:] == '\r\n' else '\n'
            lines.insert(i+1, 'fixme: true' + end)
        else:
            for j in range(len(lines)-1, i, -1):
                if lines[j].startswith('fixme: '):
                    lines.pop(j)

        with open(self.statement, 'w', newline='') as f:
            f.writelines(lines)

    def get_first_committer(self):
        cmd = ['git', 'log', '--reverse', '--format=%an%%%ae', self.path]
        out = subprocess.check_output(cmd).decode()
        name, email = out.split('\n')[0].split('%')
        return name or email

    def get_last_update(self):
        repo = git.Repository(SCRIPT_DIR)
        return repo.get_last_commit(self.path)[2] if repo.is_git_repo() else None


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
        f.write(template.render(name=params.name, problems=[problems[k] for k in params.problems], language=params.language))


def __filter_by_id_predicate(params):
    if params.id is not None:
        ids = set(params.id)
        return lambda p: p.id in ids
    else:
        return None


def __combine_predicates(*args):
    def wrapper(predicates):
        def predicate(x):
            for p in predicates:
                if not p(x):
                    return False

            return True

        return predicate

    return wrapper(list(filter(None, args)))

def problem_selector(params):
    predicates = [__filter_by_id_predicate(params)]

    if params.skip_fixme:
        predicates.append(lambda p: not p.fixme)

    if params.only_fixme:
        predicates.append(lambda p: p.fixme)

    if params.tags:
        tags = set(params.tags.split(','))
        predicates.append(lambda p: p.tags & tags)

    if params.languages:
        languages = set(params.languages.split(','))
        predicates.append(lambda p: p.languages & languages)

    if params.author:
        predicates.append(lambda p: p.author == params.author)

    return __combine_predicates(*predicates)

def find_problems(params):
    problems = []

    headers = {
        'p': 'Путь',
        'i': 'Идентификатор',
        'l': 'Название',
        't': 'Теги',
        'a': 'Автор'
    }

    for p in __find_problems(problem_selector(params)).values():
        prob = []

        for f in params.format:
            if f == 'p':
                value = os.path.relpath(p.path, PROBLEMS_DIR)
            elif f == 'i':
                value = p.id
            elif f == 'l':
                value = p.longname if len(p.longname) <= 25 or params.wide else p.longname[:24] + '…'
            elif f == 't':
                value = ' '.join(p.tags)
            elif f == 'a':
                value = p.author
            else:
                value = '?'

            prob.append(value)

        problems.append(prob)

    print(tabulate.tabulate(
        sorted(problems),
        headers=[headers.get(f, f) for f in params.format]
    ))


def find_by_id_pred(id):
    return lambda p: p.id == id


def find_problem_by_id(id):
    try:
        return next(iter(__find_problems(find_by_id_pred(id)).values()))
    except:
        print('{}: не удалось найти задачу'.format(id))


def __list_problems_on_fs():
    for root, _, files in os.walk(PROBLEMS_DIR):
        for file in files:
            fname, fext = os.path.splitext(file.lower())
            if fname == 'statement' and fext[1:] in ALLOWED_MD_LANGS:
                ppath = os.path.join(root, file)
                try:
                    problem = Problem(ppath)
                    if problem.errors:
                        print(problem.format_errors())
                    yield problem
                except:
                    print('Ошибка при загрузке условия: {}'.format(ppath))
                    if args.verbose:
                        traceback.print_exc()


def __list_problems_in_cache():
    with open(CACHE_FILE, 'rb') as f:
        return pickle.load(f)


def __find_problems(predicate=None):

    problems = {}

    probs = __list_problems_in_cache() if os.path.isfile(CACHE_FILE) else __list_problems_on_fs()

    for problem in probs:
        if predicate and not predicate(problem):
            continue

        if problem.id in problems:
            print('{}: не уникальный id'.format(problem.path))
        else:
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
        shortname = pb.problem_shortname(k, len(ids))
        prob = problems_dict[p]
        prob.metadata['shortname'] = shortname
        prob.metadata.update(problem_overrides.get(prob.id))

    problems = [problems_dict[p] for p in ids]

    template_file = params.template if params.template != 'auto' else '{}-ejudge.cfg.jinja2'.format(desc['language'])
    template = env.get_template(template_file)

    with open(os.path.join(conf_dir, 'serve.cfg'), 'w') as f:
        f.write(template.render(problems=problems, language=desc['language']))

    md = markdown.Markdown(extensions = ['markdown.extensions.tables', InputOutputExamplesExtension()])
    for p in problems:
        problem_dir = os.path.join(problems_dir, p.metadata['shortname'])
        os.makedirs(problem_dir, exist_ok=True)
        with open(os.path.join(statements_dir, p.metadata['shortname'] + ".html"), 'w') as f:
            html = md.convert(p.content)
            f.write(bs4.BeautifulSoup(html, 'lxml').prettify())
        generate_tests_for_problem(p)
        if p.checker is None:
            shutil.copy(os.path.join(p.path, CHECKER), problem_dir)
        for c in [p.get_header, p.get_footer]:
            c_path = c(desc['language'])
            if c_path:
                shutil.copy(c_path, problem_dir)
        shutil.copytree(p.tests_dir, os.path.join(problem_dir, TESTS_FOLDER))

    if params.summary:
        print('Задачи контеста:')

        print(tabulate.tabulate(
            [(prob.metadata['shortname'], prob.id, prob.longname) for prob in map(problems_dict.get, ids)],
            headers=['Короткое название', 'Идентификатор', 'Название']
        ))


def generate_tests_for_problem(prob, force=False):

    if prob.has_tests() and not force:
        print('Пропускаю генерацию тестов для ' + prob.path)
        return True

    print('Генерирую тесты для ' + prob.path)

    try:
        prob.generate_tests()
        status = True
    except subprocess.CalledProcessError as e:
        print("Ошибка при генерации тестов для {}: {}".format(prob.path, e.output.decode()))
        status = False

    return status


def __generate_tests(params):
    problems = __find_problems(problem_selector(params))

    with multiprocessing.Pool(params.jobs) as p:
        return dict(zip(
            problems.keys(),
            p.map(functools.partial(generate_tests_for_problem, force=params.force_overwrite), problems.values())
        ))

# FIXME
def generate_tests(params):
    for s in __generate_tests(params).values():
        if not s:
            return -1


def validate_problem(prob, params):
    if params.verbose:
        print('Проверка задачи:', prob.path)

    prob.validate(check_checksum=not params.ignore_checksum, check_solution=True, check_codestyle=not params.ignore_codestyle)

    # FIXME
    allowed_errors = set((params.allowed_errors if 'allowed_errors' in params else None) or [])
    status = MARK_FAILED if any(filter(lambda e: e[0] not in allowed_errors, prob.errors)) else MARK_OK

    tests = MARK_FAILED if prob.has_error_occurred(Problem.ERROR_TESTS_MISSING) else MARK_OK
    test_generator = MARK_FAILED if prob.has_error_occurred(Problem.ERROR_TEST_GENERATOR_MISSING) else MARK_OK

    if prob.has_error_occurred(Problem.ERROR_TEST_DUPLICATES):
        unique_tests = MARK_FAILED
    elif prob.has_error_occurred(Problem.ERROR_TESTS_MISSING):
        unique_tests = MARK_UNKNOWN
    else:
        unique_tests = MARK_OK

    if prob.has_error_occurred(Problem.ERROR_SOLUTION_MISSING):
        solution = MARK_UNKNOWN
    elif prob.has_error_occurred(Problem.ERROR_TEST_FAILED) or prob.has_error_occurred(Problem.ERROR_SOLUTION_COMPILATION):
        solution = MARK_FAILED
    else:
        solution = MARK_OK

    if prob.has_error_occurred(Problem.ERROR_CHECKSUM_MISSING) or params.ignore_checksum:
        checksum = MARK_UNKNOWN
    elif prob.has_error_occurred(Problem.ERROR_CHECKSUM_MISMATCH):
        checksum = MARK_FAILED
    else:
        checksum = MARK_OK

    if params.update_fixme:
        prob.mark_fixme(status == MARK_FAILED)

    return prob, tests, unique_tests, test_generator, solution, checksum, status


def validate_problems(params):
    problems = __find_problems(problem_selector(params)).values()

    if params.ignore_checksum and params.verbose:
        print("Проверка контрольных сумм отключена")

    with multiprocessing.Pool(params.jobs) as p:
        return list(p.map(functools.partial(validate_problem, params=params), problems))


def print_validation_results(results, verbose=False):
    if len(results) == 0:
        return

    report = []
    failed = False
    for k, (prob, tests, unique_tests, test_generator, solution, checksum, status) in enumerate(results):
        report.append([k + 1, prob.id, prob.longname, tests, unique_tests, test_generator, solution, checksum, status])

        failed = failed or prob.errors

        if prob.errors and verbose:
            print(prob.format_errors())

    print(tabulate.tabulate(
        report,
        headers=['#', 'Идентификатор', 'Название', 'Тесты', 'Уникальные тесты', 'Генератор тестов', 'Решение',
                 'Контрольная сумма', 'Статус']
    ))

    return not failed


def validate(params):

    results = validate_problems(params)

    if print_validation_results(results, params.verbose):
        return 0
    else:
        return 1


def show(params):
    prob = find_problem_by_id(params.id)

    if prob is None:
        print('Задача не найдена')
        return -1

    with open(prob.statement) as f:
        print(f.read())


def edit(params):
    problem = find_problem_by_id(params.id)

    if problem is None:
        print('Задача не найдена')
        return -1

    editor = subprocess.check_output(['which', os.environ.get('EDITOR', 'vim')]).decode('utf-8').strip()
    os.execl(editor, editor, problem.statement)


def info(params):
    prob = find_problem_by_id(params.id)

    if prob is None:
        print('Задача не найдена')
        return -1

    print('id:', prob.id)
    print('Название:', prob.longname)
    print('Путь:', prob.path)
    print('Теги:', ', '.join(prob.tags))


def commit(params):
    problem = find_problem_by_id(params.id)

    if problem.has_checksum() and not params.force_overwrite:
        print('{}: текущее состояние задачи уже зафиксировано, используйте --force-overwrite для перезаписи'.format(problem.path))
        sys.exit(-1)

    problem.validate(check_checksum=False, check_solution=True)
    if problem.errors:
        print(problem.format_errors())
        print('{}: устраните ошибки перед тем, как фиксировать состояние задачи'.format(problem.path))
        sys.exit(-1)

    problem.commit()
    problem.validate()


def list_tags(params):
    tags = {}

    for p in __find_problems().values():
        for t in p.tags:
            tags[t] = tags.get(t, 0) + 1

    print(tabulate.tabulate(
        sorted(tags.items()),
        headers=['Тэг', 'Количество задач']
    ))


def fixme(params):
    predicate = __filter_by_id_predicate(params)

    for prob in __find_problems(predicate).values():
        prob.mark_fixme(not params.unset)


def __github_login():
    def two_factor_callback():
        code = None
        while not code:
            code = input('Код для двухфакторной аутентификации: ')

        return code

    user = None
    while not user:
        user = input('Имя пользователя: ')

    try:
        with open(CREDENTIALS_FILE, 'r') as f:
            token, id = map(str.strip, f.readlines())
            return github3.login(user, token)
    except IOError:

        password = None
        while not password:
            password = getpass.getpass('Пароль для {0}: '.format(user))

        note = 'contest.py'
        note_url = 'https://github.com/mipt-cs/problembook'
        scopes = ['user', 'repo']

        auth = github3.authorize(user, password, scopes, note, note_url, two_factor_callback=two_factor_callback)

        with open(CREDENTIALS_FILE, 'w') as f:
            f.write(auth.token + '\n')
            f.write(str(auth.id))

        return github3.login(user, auth.token)


def review(params):
    predicate = __filter_by_id_predicate(params)

    gh = __github_login()

    repo = gh.repository('mipt-cs', 'problembook')

    template = jinja2.Environment(loader=jinja2.BaseLoader).from_string(ISSUE_BODY)

    for prob in __find_problems(predicate).values():
        if prob.fixme:
            if args.verbose:
                print('Создаю тикет для задачи:', prob.longname)
            path = prob.path[len(SCRIPT_DIR)+1:]
            title = 'Ревью: ' + prob.longname
            langs = []
            missed_langs = []
            for lang in EXTENSION_MAP:
                if prob.get_solution(lang):
                    langs.append(lang)
                else:
                    missed_langs.append(lang)
            body = template.render(id=prob.id, path=path, langs=langs, missed_langs=missed_langs, has_checker=prob.has_checker())
            while True:
                try:
                    repo.create_issue(title=title, body=body, labels=['review', 'help wanted'])
                    break
                except github3.exceptions.ForbiddenError:
                    if args.verbose:
                        print('Ошибка при создании тикета, пауза 30 секунд…')
                    time.sleep(30)


def mega_contest(params):

    repo = git.Repository(SCRIPT_DIR)

    if not repo.check_tree_is_clean():
        print('Создание мега-контеста предполагает активное переключение веток в текущем репозитории, '
              'поэтому перед запуском команды убедитесь, что незакомиченные изменения отсутствуют')

        return -1

    root = tempfile.mkdtemp()
    problems_dir = os.path.join(root, 'problems')

    for dir in 'lib', 'templates':
        shutil.copytree(os.path.join(SCRIPT_DIR, dir), os.path.join(root, dir))

    shutil.copy(__file__, os.path.join(root, 'contest.py'))

    os.mkdir(problems_dir)

    cur_branch = repo.get_current_branch()

    problems_map = {}

    find_params = problem_selector(
        pb.FakeArgs(
            language=params.language,
            skip_fixme=False
        )
    )

    for branch in repo.list_branches():
        print('Обрабатываю бранч', branch)
        repo.checkout_branch(branch)

        for id, prob in __find_problems(find_params).items():
            update = False
            if id not in problems_map:
                update = True
            elif prob.last_update > problems_map[id][1]:
                update = True

            if update:
                problems_map[id] = branch, prob.last_update

    branch_map = {}

    for id, (branch, _) in problems_map.items():
        if branch not in branch_map:
            branch_map[branch] = []
        branch_map[branch].append(id)

    print('Статистика по задачам из разных бранчей:')
    stats = sorted(((len(ids), branch) for branch, ids in branch_map.items()), reverse=True)
    for count, branch in stats:
        print('  ', branch, ': ', count, sep='')

    print('Всего: ', sum(map(pb.first, stats)))

    mega_contest = {
        'name': params.id,
        'language': params.language,
        'problems': []
    }

    for branch, probs in branch_map.items():
        print('Обрабатываю задачи из бранча', branch)

        repo.checkout_branch(branch)

        generated_tests = generate_tests(pb.FakeArgs(
            id=probs,
            language=params.language,
            jobs=params.jobs,
            force_overwrite=True,
            skip_fixme=True
        ))

        tasks_to_validate = list(map(
            pb.first,
            filter(
                pb.second,
                generated_tests.items()
            )
        ))

        print('Количество задач, для которых сгенерированы тесты:', len(tasks_to_validate))

        validated_problems = validate_problems(pb.FakeArgs(
            id=tasks_to_validate,
            ignore_checksum=True,
            check_solution=True,
            ignore_codestyle=True,
            allowed_errors=[Problem.ERROR_TEST_DUPLICATES]
        ))

        print_validation_results(validated_problems)

        good_problems = list(map(
            pb.first,
            filter(
                lambda x: x[1] == MARK_OK and x[4] == MARK_OK,
                validated_problems
            )
        ))

        print('Количество минимально готовых задач:', len(good_problems))

        for prob in good_problems:
            rel_path = os.path.relpath(prob.path, SCRIPT_DIR)
            target_path = os.path.join(root, rel_path)
            shutil.copytree(prob.path, target_path)

            mega_contest['problems'].append({
                prob.id: {
                    'score': 1000
                }
            })


    repo.checkout_branch(cur_branch)

    with open(os.path.join(root, 'mega.yml'), 'w') as f:
        yaml.dump(mega_contest, f)

    subprocess.check_call([
        sys.executable, 'contest.py',
        'ejudge',
        '-o', root,
        '-s',
        'mega.yml'
    ], cwd=root)


def cache(params):
    if params.clear:
        if os.path.isfile(CACHE_FILE):
            os.remove(CACHE_FILE)
    elif params.make:
        probs = list(__list_problems_on_fs())
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(probs, f)


if __name__ == "__main__":

    os.environ['PYTHONPATH'] = '{}{}{}'.format(SCRIPT_DIR, os.pathsep, os.environ.get('PYTHONPATH', ''))

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
    create_problem_parser.add_argument('-G', '--languages', default='', help='Список языков через запятую')

    create_contest_parser = subparsers.add_parser('create-contest', help='Создать контест')
    create_contest_parser.set_defaults(_action=create_contest)
    create_contest_parser.add_argument('-n', '--name', required=True, help='Название контеста')
    create_contest_parser.add_argument('-l', '--language', required=True, help='Язык контеста')
    create_contest_parser.add_argument('-f', '--force-overwrite', action='store_true', help='Перезаписывать существующие конфиги контестов')
    create_contest_parser.add_argument('problems', nargs='+', help='Список идентификаторов задач')

    find_problems_parser = subparsers.add_parser('find-problems', help='Найти задачи')
    find_problems_parser.add_argument('id', nargs='*', help='Идентификатор задачи')
    find_problems_parser.add_argument('-s', '--skip-fixme', action='store_true', help='Пропускать задачи с меткой "fixme: true"')
    find_problems_parser.add_argument('--only-fixme', action='store_true', help='Только задачи с меткой "fixme: true"')
    find_problems_parser.add_argument('-t', '--tags', help='Список тэгов')
    find_problems_parser.add_argument('-l', '--languages', help='Список языков')
    find_problems_parser.add_argument('--author', help='Только задачи указанного автора (по первому комиту)')
    find_problems_parser.add_argument('-w', '--wide', action='store_true', help='Не обрезать описания задач')
    find_problems_parser.add_argument('-f', '--format', default='pilt', action='store', help='Список колонок для вывода. По-умолчания — (p) путь, (i) идентификатор, (l) название, (t) тэги')
    find_problems_parser.set_defaults(_action=find_problems)

    generate_ejudge_config_parser = subparsers.add_parser('ejudge', help='Сгенерировать конфиг ejudge')
    generate_ejudge_config_parser.set_defaults(_action=generate_ejudge_config)
    generate_ejudge_config_parser.add_argument('contest', help='Файл с описание контеста')
    generate_ejudge_config_parser.add_argument('-t', '--template', default='auto', help='Шаблон конфига')
    generate_ejudge_config_parser.add_argument('-o', '--output-dir', required=True, help='Выходной путь')
    generate_ejudge_config_parser.add_argument('-f', '--force-overwrite', action='store_true', help='Перезаписывать существующие конфиги ejudge')
    generate_ejudge_config_parser.add_argument('-s', '--summary', action='store_true', help='Вывести короткие имена для задач  в контесте')

    generate_tests_parser = subparsers.add_parser('generate-tests', help='Сгенерировать тесты')
    generate_tests_parser.set_defaults(_action=generate_tests)
    generate_tests_parser.add_argument('id', nargs='*', help='Идентификатор задачи')
    generate_tests_parser.add_argument('-j', '--jobs', default=1, type=int, help='Количество параллельных потоков для генерации')
    generate_tests_parser.add_argument('-f', '--force-overwrite', action='store_true', help='Перезаписывать существующие тесты')
    generate_tests_parser.add_argument('-s', '--skip-fixme', action='store_true', help='Пропускать задачи с меткой "fixme: true"')
    generate_tests_parser.add_argument('--only-fixme', action='store_true', help='Только задачи с меткой "fixme: true"')
    generate_tests_parser.add_argument('-t', '--tags', help='Список тэгов')
    generate_tests_parser.add_argument('-l', '--languages', help='Список языков')
    generate_tests_parser.add_argument('--author', help='Только задачи указанного автора (по первому комиту)')

    validate_parser = subparsers.add_parser('validate', help='Проверить корректность условий в репозитории')
    validate_parser.add_argument('id', nargs='*', help='Идентификатор задачи')
    validate_parser.add_argument('-I','--ignore-checksum', action='store_true', help='Не учитывать контрольную сумму в статусе валидации')
    validate_parser.add_argument('-C','--ignore-codestyle', action='store_true', help='Не проверять стиль кода')
    validate_parser.add_argument('-j', '--jobs', default=1, type=int, help='Количество параллельных потоков для проверки')
    validate_parser.add_argument('-s', '--skip-fixme', action='store_true', help='Пропускать задачи с меткой "fixme: true"')
    validate_parser.add_argument('--only-fixme', action='store_true', help='Только задачи с меткой "fixme: true"')
    validate_parser.add_argument('-t', '--tags', help='Список тэгов')
    validate_parser.add_argument('-l', '--languages', help='Список языков')
    validate_parser.add_argument('--author', help='Только задачи указанного автора (по первому комиту)')
    validate_parser.add_argument('--update-fixme', action='store_true',
                                 help='Автоматически проставить fixme для задач ' \
                                 'не прошедших валидацию и убрать fixme для ' \
                                 'прошедших')
    validate_parser.set_defaults(_action=validate)

    show_parser = subparsers.add_parser('show', help='Показать описание задачи')
    show_parser.set_defaults(_action=show)
    show_parser.add_argument('id', help='Идентификатор задачи')

    edit_parser = subparsers.add_parser('edit', help='Отредактировать описание задачи')
    edit_parser.set_defaults(_action=edit)
    edit_parser.add_argument('id', help='Идентификатор задачи')

    info_parser = subparsers.add_parser('info', help='Показать информацию по задаче')
    info_parser.set_defaults(_action=info)
    info_parser.add_argument('id', help='Идентификатор задачи')

    commit_parser = subparsers.add_parser('commit', help='Зафиксировать состояние задачи')
    commit_parser.set_defaults(_action=commit)
    commit_parser.add_argument('id', help='Идентификаторы задач')
    commit_parser.add_argument('-f', '--force-overwrite', action='store_true', help='Перезаписать контрольные суммы')

    list_tags_parser = subparsers.add_parser('list-tags', help='Вывести список тэгов')
    list_tags_parser.set_defaults(_action=list_tags)

    fixme_parser = subparsers.add_parser('fixme', help='Добавить/снять метку fixme для задачи')
    fixme_parser.add_argument('-u', '--unset', action='store_true', help='Снять метку')
    fixme_parser.add_argument('id', nargs='*', help='Идентификатор задачи')
    fixme_parser.set_defaults(_action=fixme)

    review_parser = subparsers.add_parser('review', help='Открыть на Github тикет на ревью')
    review_parser.add_argument('id', nargs='*', help='Идентификатор задачи')
    review_parser.set_defaults(_action=review)

    mega_contest_parser = subparsers.add_parser('mega-contest', help='Создать «мега-контест» из всех задач')
    mega_contest_parser.add_argument('-l', '--language', required=True, help='Язык контеста')
    mega_contest_parser.add_argument('-j', '--jobs', default=1, type=int, help='Количество параллельных потоков для генерации')
    mega_contest_parser.add_argument('-i', '--id', required=True, help='Идентификатор контеста в ejudge')
    mega_contest_parser.set_defaults(_action=mega_contest)

    cache_parser = subparsers.add_parser('cache', help='Работа с кэшем для быстрого поиска задач')
    cache_parser.set_defaults(_action=cache)
    group = cache_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--make', action='store_true', help='Создать кэш')
    group.add_argument('-c', '--clear', action='store_true', help='Очистить кэш')

    args = parser.parse_args()

    if 'id' in args and args.id == []:
        args.id = None

    sys.exit(args._action(args) or 0)
