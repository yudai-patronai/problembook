a = input()


def check_bracket_seq(seq):
  stack = []
  for el in seq:
    if el == '[':
      stack.append('[')
    elif el == ']' and stack[-1] == '[':
      stack.pop()
    elif el == ']' and stack[-1] != '[':
      return 'NO'
    elif el == '(':
      stack.append('(')
    elif el == ')' and stack[-1] == '(':
      stack.pop()
    elif el == ')' and stack[-1] != '(':
      return 'NO'
    elif el == '{':
      stack.append('{')
    elif el == '}' and stack[-1] == '{':
      stack.pop()
    elif el == '}' and stack[-1] != '{':
      return 'NO'
  if stack:
    return 'NO'
  else:
    return 'YES'


check_bracket_seq(a)