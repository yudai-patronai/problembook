#!/usr/bin/env python3

import os
import sys
import random

sys.path.append(os.path.abspath('../..'))
import task

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

task.gen_tests_weight_adj(tests_dir)
