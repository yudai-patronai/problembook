'''

assert not ("*" in prog), "Use of '*' is forbidden!"
assert not ("/" in prog), "Use of '/' is forbidden!"
assert not ("//" in prog), "Use of '//' is forbidden!"
assert not ("%" in prog), "Use of '%' is forbidden!"

exec(prog)