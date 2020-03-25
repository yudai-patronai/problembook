#!/usr/bin/env python3


def list_to_array(linked_list, head):
    key, next_pos = head
    array = [key]
    while next_pos != -1:
        key, next_pos = linked_list[next_pos]
        array.append(key)
    return array
