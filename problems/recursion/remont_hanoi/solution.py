def mov (n, start, finish):
    if n > 0:
        if (start + finish) == 4:
            return mov (n, start, 2) + mov (n, 2, finish)
        else:
            return mov (n-1, start, 6-start-finish)+[[n, start, finish]]+ mov (n-1, 6-start-finish, finish)
    else:
        return []
