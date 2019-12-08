def chanoi(disc, start, other, finish):
    if disc < 2:
        if (3 + start - finish) % 3 == 1:
            return [[1, start, other], [1, other, finish]]
        else:
            return [[1, start, finish]]
    else:
        if (3 + start - finish) % 3 == 1:
            result = chanoi(disc - 1, start, other, finish)
            result += [[disc, start, other]]
            result += chanoi(disc - 1, finish, other, start)
            result += [[disc, other, finish]]
            result += chanoi(disc - 1, start, other, finish)
            return result
        else:
            result = chanoi(disc - 1, start, finish, other)
            result += [[disc, start, finish]]
            result += chanoi(disc - 1, other, start, finish)
            return result
