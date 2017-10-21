#!/usr/bin/env python3

import os
import sys
import yaml
import subprocess
import tempfile
import shutil

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTEST_PY = os.path.join(DIR, 'contest.py')
CONTEST_LIST = os.path.join(DIR, '.active-contests.yml')

ADDRESS = 'judge2.vdi.mipt.ru'
USER = 'ejudge'
PORT = 22
PATH = '/home/judges'

# rsync -e "ssh -p $(SSH_PORT)" - P - rvzc - -delete $(OUTPUTDIR) / $(SSH_USER) @$(SSH_HOST):$(SSH_TARGET_DIR) - -cvs - exclude

if not os.path.isfile(CONTEST_LIST):
    print('Не найден список активных контестов')
    sys.exit(0)

with open(CONTEST_LIST) as f:
    cfg = yaml.load(f)

for contest, ids in cfg['contests'].items():
    d = tempfile.mkdtemp()
    subprocess.check_call([sys.executable, CONTEST_PY, 'ejudge', '-o', d, os.path.join(DIR, 'contests', '{}.yml'.format(contest))])
    path = os.path.join(d, contest)
    for _id in ids:
        new_path = os.path.join(d, str(_id))
        os.rename(path, new_path)
        subprocess.check_call([
            'rsync',
            '-e', 'ssh -p {}'.format(PORT),
            '-Prvzc', '--delete',
            '--cvs-exclude',
            new_path, '{}@{}:{}'.format(USER, ADDRESS, PATH)
        ])
        os.rename(new_path, path)
    shutil.rmtree(d)