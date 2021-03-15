# задача является подобием задачи sort/livejournal, но версия для множеств

def read_set():
    x = set()
    for _ in range(int(input())):
        x.add(input())
    return x


following = read_set()
followers = read_set()

mutual = following & followers
fans = followers - mutual
heroes = following - mutual

print(len(mutual), len(fans), len(heroes))
