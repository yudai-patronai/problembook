'''

assert not ("[" in prog), "Use of lists is forbidden!"
assert not ("list(" in prog), "Use of lists is forbidden!"

exec(prog)