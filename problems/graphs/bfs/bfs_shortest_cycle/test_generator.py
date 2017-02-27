#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.abspath('..'))
import task

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
task.gen_tests_directed(tests_dir)
