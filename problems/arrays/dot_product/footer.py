
if __name__ == "__main__":
    vec1 = [int(x) for x in input().split(" ")]
    vec2 = [int(x) for x in input().split(" ")]
    print(dot_product(len(vec1), vec1, vec2))