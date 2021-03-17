
if __name__ == "__main__":
    linked_list = []
    for pairs in input().split('\t'):
        key, value = [int(e) for e in pairs.split(' ')]
        linked_list.append((key, value))
    head = linked_list.pop()
    array = list_to_array(linked_list, head)
    print(*array)
