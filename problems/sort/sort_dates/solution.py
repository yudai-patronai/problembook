def sort_key(date_entry):
    # year, month, day, hours, minutes

    return date_entry[2], monthes.index(date_entry[1]), date_entry[0], date_entry[3], date_entry[4]


N = int(input())
dates = []

monthes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for _ in range(N):
    d = input().split()
    day = int(d[0])
    month = d[1]
    year = int(d[2])
    hh, mm = map(int, d[3].split(':'))
    dates.append([day, month, year, hh, mm])

dates.sort(key=sort_key)

for d in dates:
    print( '{} {} {} {}:{:02d}'.format(*d) )
