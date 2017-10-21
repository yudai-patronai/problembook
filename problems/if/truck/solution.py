#!/usr/bin/env python3

truck_w = int(input())
truck_h = int(input())
piano_w = int(input())
piano_h = int(input()) + truck_h
fridge_w = int(input())
fridge_h = int(input()) + truck_h
max_w = int(input())
max_h = int(input())

if truck_w + piano_w + fridge_w <= max_w:
    if fridge_h <= max_h:
        print('YES')
    else:
        print('NO')
elif piano_h <= max_h and fridge_h <= max_h:
    if truck_w + piano_w <= max_w:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
