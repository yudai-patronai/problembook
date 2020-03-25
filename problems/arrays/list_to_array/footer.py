#!/usr/bin/env python3

if __name__ == "__main__":
    linked_list = []
    for el in input().split('\t'): 
        key, value = [int(e) for e in el.split(' ')] 
        linked_list.append((key, value))
    # input format: key0 next0 \t key1 next1 \t ... \t key_head next_key
    head = linked_list.pop()
    array = list_to_array(linked_list, head)
    print(*array)
