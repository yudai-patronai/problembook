#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.abspath('..'))
import testgen

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
testgen.gen_tests(tests_dir)
