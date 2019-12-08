dlist = {}
mlist = {}
cnt = int(input())
for i in range(cnt):
    tls = input().split()
    bname = ' '.join(tls[1:])
    if tls[0] == 'desktop':
        dlist[bname] = dlist.get(bname, 0) + 1
    else:
        mlist[bname] = mlist.get(bname, 0) + 1
dlist = sorted(dlist.items(), key = lambda x: x[1], reverse = True)
mlist = sorted(mlist.items(), key = lambda x: x[1], reverse = True)
if len(dlist) > 0:
    print('desktop browsers raiting')
    i = 0
    snum = 0
    for x in dlist:
        i += 1
        if snum < i:
            pcnt = 0;
            for y in dlist:
                if y[1] == x[1]:
                    pcnt += 1
            snum += pcnt
            if pcnt == 1:
                nsamp = str(i)
            else:
                nsamp = str(i) + " - " + str(i + pcnt - 1)
        print(nsamp, x[0])
if len(mlist) > 0:
    print('mobile browsers raiting')
    i = 0
    snum = 0
    for x in mlist:
        i += 1
        if snum < i:
            pcnt = 0;
            for y in mlist:
                if y[1] == x[1]:
                    pcnt += 1
            snum += pcnt
            if pcnt == 1:
                nsamp = str(i)
            else:
                nsamp = str(i) + " - " + str(i + pcnt - 1)
        print(nsamp, x[0])
