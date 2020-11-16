
f = eval("lambda x: {}".format(input()))
left = float(input())
right = float(input())


x, fx = ternary_search(f, left, right)
print("{:.5} {:.5}".format(x, fx))
