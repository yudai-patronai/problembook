#!/usr/bin/env python3

import os
from lib import random

from lib.graphs import task

random.seed('acyclic')

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
task.gen_tests_directed(tests_dir)
