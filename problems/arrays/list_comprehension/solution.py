def list_filter(lst):
    return [x * 2 if x > 10 else x - 5 for x in lst if x != 3]
