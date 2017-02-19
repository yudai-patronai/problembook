#!/usr/bin/python3

import argparse
import os
import sys
import shutil
import uuid
import jinja2
import frontmatter
import tabulate
import yaml
import markdown
import bs4

#ALLOWED_MD_LANGS = ['md', 'rst']
ALLOWED_MD_LANGS = ['md']
SCRIPT_DIR = os.path.dirname(__file__)
PROBLEMS_DIR = os.path.join(SCRIPT_DIR, 'problems')
CONTESTS_DIR = os.path.join(SCRIPT_DIR, 'contests')

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(SCRIPT_DIR, 'templates')),
)

def create_problem(params):
    lng = params.markdown_language

    template = env.get_template('problem.{}.jinja2'.format(lng))

    problem_dir = os.path.join(PROBLEMS_DIR, params.path)
    os.makedirs(problem_dir, exist_ok=True)

    with open(os.path.join(problem_dir, 'statement.' + lng), 'w') as f:
        f.write(template.render(id=str(uuid.uuid4()), **params.__dict__))


def create_contest(params):
    os.makedirs(CONTESTS_DIR, exist_ok=True)

    problems = __find_problems(lambda p: p['id'] in params.problems)

    contest_file = os.path.join(CONTESTS_DIR, "{}.yml".format(params.name))
    if os.path.isfile(contest_file):
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
                if predicate and not predicate(problem):
                    continue
                problems.append(problem)
                k += 1

    return problems


def generate_ejudge_config(params):
    with open(params.contest) as f:
        desc = yaml.load(f)

    root_dir = os.path.join(params.output_dir, desc['name'])
    if os.path.isdir(root_dir):
        sys.stderr.write('Директория {} уже существует.'.format(root_dir))
        sys.exit(-1)

    conf_dir = os.path.join(root_dir, 'conf')
    problems_dir = os.path.join(root_dir, 'problems')

    os.makedirs(conf_dir, exist_ok=True)
    os.makedirs(problems_dir, exist_ok=True)

    ids = set(list(p.keys())[0] for p in desc['problems'])
    problems = __find_problems(lambda p: p['id'] in ids)
    for k, p in enumerate(problems):
        p.metadata['shortname'] = chr(ord('A') + k)

    template = env.get_template(params.template)

    with open(os.path.join(conf_dir, 'serve.cfg'), 'w') as f:
        f.write(template.render(problems=map(lambda p: p.metadata, problems)))

    for p in problems:
        problem_dir = os.path.join(problems_dir, p.metadata['shortname'])
        os.makedirs(problem_dir, exist_ok=True)
        with open(os.path.join(problem_dir, 'statement.html'), 'w') as f:
            html = markdown.markdown(p.content, extensions = ['markdown.extensions.tables'])
            f.write(bs4.BeautifulSoup(html, 'lxml').prettify())
        shutil.copytree(os.path.join(p.metadata['path'], 'tests'), os.path.join(problem_dir, 'tests'))


parser = argparse.ArgumentParser(prog='contest')
subparsers = parser.add_subparsers(dest='cmd')
subparsers.required = True

create_problem_parser = subparsers.add_parser('create-problem', help='Создать задачу')
create_problem_parser.set_defaults(_action=create_problem)
create_problem_parser.add_argument('-p', '--path', required=True, help='Путь, по которому будет создана задача')
create_problem_parser.add_argument('-t', '--tags', default='', help='Список тегов через запятую')
create_problem_parser.add_argument('-L', '--markdown-language', default=ALLOWED_MD_LANGS[0], choices=ALLOWED_MD_LANGS, help='Язык разметки')
create_problem_parser.add_argument('-l', '--longname', help='Длинное название')

create_contest_parser = subparsers.add_parser('create-contest', help='Создать контест')
create_contest_parser.set_defaults(_action=create_contest)
create_contest_parser.add_argument('-n', '--name', required=True, help='Название контеста')
create_contest_parser.add_argument('problems', nargs='+', help='Название контеста')

find_problems_parser = subparsers.add_parser('find-problems', help='Найти задачи')
find_problems_parser.set_defaults(_action=find_problems)

generate_ejudge_config_parser = subparsers.add_parser('ejudge', help='Сгенерировать конфиг ejudge')
generate_ejudge_config_parser.set_defaults(_action=generate_ejudge_config)
generate_ejudge_config_parser.add_argument('contest', help='Файл с описание контеста')
generate_ejudge_config_parser.add_argument('-t', '--template', required=True, help='Шаблон конфига')
generate_ejudge_config_parser.add_argument('-o', '--output-dir', required=True, help='Выходной путь')

args = parser.parse_args()

args._action(args)

