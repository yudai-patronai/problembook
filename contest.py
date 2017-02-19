#!/usr/bin/python3

import argparse
import os
import uuid
import jinja2

SCRIPT_DIR = os.path.dirname(__file__)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(SCRIPT_DIR, 'templates')),
)

def create_problem(params):
    lng = params.markdown_language

    template = env.get_template('problem.{}.jinja2'.format(lng))

    problem_dir = os.path.join(SCRIPT_DIR, 'problems', params.path)
    os.makedirs(problem_dir, exist_ok=True)

    with open(os.path.join(problem_dir, 'statement.' + lng), 'w') as f:
        f.write(template.render(id=str(uuid.uuid4()), **params.__dict__))


parser = argparse.ArgumentParser(prog='contest')
subparsers = parser.add_subparsers(dest='cmd')
subparsers.required = True

create_problem_parser = subparsers.add_parser('create-problem', help='Создать задачу')
create_problem_parser.set_defaults(_action=create_problem)
create_problem_parser.add_argument('-p', '--path', required=True, help='Путь, по которому будет создана задача')
create_problem_parser.add_argument('-t', '--tags', default='', help='Список тегов через запятую')
create_problem_parser.add_argument('-L', '--markdown-language', default='md', choices=['md'], help='Язык разметки')
create_problem_parser.add_argument('-s', '--shortname', help='Короткое название')
create_problem_parser.add_argument('-l', '--longname', help='Длинное название')

args = parser.parse_args()

args._action(args)

