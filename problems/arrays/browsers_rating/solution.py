def report_one(lst):
    i = 0
    snum = 0
    for x in lst:
        i += 1
        if snum < i:
            pcnt = 0
            for y in lst:
                if y[1] == x[1]:
                    pcnt += 1
            snum += pcnt
            if pcnt == 1:
                nsamp = str(i)
            else:
                nsamp = str(i) + " - " + str(i + pcnt - 1)
        print(nsamp, x[0])


def report_all(l1, l2):
    if len(l1) > 0:
        print('desktop browsers rating')
        report_one(l1)
    if len(l2) > 0:
        print('mobile browsers rating')
        report_one(l2)


dlist = {}
mlist = {}
cnt = int(input())
for i in range(cnt):
    mst = input()
    tls = mst.split()
    bname = ' '.join(tls[1:])
    if tls[0] == 'desktop':
        dlist[bname] = dlist.get(bname, 0) + 1
    else:
        mlist[bname] = mlist.get(bname, 0) + 1
dlist = sorted(dlist.items(), key=lambda x: x[1], reverse=True)
mlist = sorted(mlist.items(), key=lambda x: x[1], reverse=True)
report_all(dlist, mlist)
