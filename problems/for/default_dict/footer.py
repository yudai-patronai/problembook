if __name__ == "__main__":
    elems = list(map(int, input().split()))
    PREFIX = elems.pop(0)
    pc = PrefixClass(PREFIX)
    dct = defaultdict(pc)
    result_list = [dct[elem] for elem in elems]
    print(''.join(result_list))
