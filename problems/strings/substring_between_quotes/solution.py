s = input()

start = s.find('"')
finish = s.rfind('"')

print(s[start+1:finish])
