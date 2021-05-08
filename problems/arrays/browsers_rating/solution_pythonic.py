from collections import OrderedDict


def report_group(place, group):
    place_last = place if len(group) == 1 else place + len(group) - 1
    place_prefix = '{} - {}'.format(place, place_last) if place != place_last else str(place)
    for name in group:
        print(place_prefix, name)
    return place + len(group)

def report_rating(counters):
    # rating_list = sorted(counters.items(), key=lambda x: x[0])  # по названиям
    # rating_list.sort(key=lambda x: x[1], reverse=True)          # + по голосам
    
    rating_list = sorted(counters.items(), key=lambda x: x[1], reverse=True)
    
    place_count, group, place =  -1, [], 1
    for name, count in rating_list:
        if place_count == count:
            group.append(name)
        else:
            if group:
                place = report_group(place, group)
            group = [name]
            place_count = count
    if group:  # last
        report_group(place, group)


desktop = OrderedDict()
mobile = OrderedDict()
for _ in range(int(input())):
    platform, name = input().split(maxsplit=1)
    if platform == 'desktop':
        desktop[name] = desktop.get(name, 0) + 1
    else:
        mobile[name] = mobile.get(name, 0) + 1

if len(desktop):
    print('desktop browsers rating')
    report_rating(desktop)
if len(mobile):
    print('mobile browsers rating')
    report_rating(mobile)
