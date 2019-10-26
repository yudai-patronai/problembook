time1 = input()
time2 = input()
h1, m1, s1 = time1.split(':')
h2, m2, s2 = time2.split(':')
ss1 = int(s1) + int(m1)*60 + int(h1)*60*60
ss2 = int(s2) + int(m2)*60 + int(h2)*60*60
if (ss1 <= ss2):
    print(ss2 - ss1)
else:
    diff = 24*60*60 - ss1 + ss2
    print(diff)
