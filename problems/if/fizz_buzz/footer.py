"""

assert not ("/" in program), "Use of '/' is forbidden!"
assert not ("//" in program), "Use of '//' is forbidden!"
assert not ("%" in program), "Use of '%' is forbidden!"

exec(program)