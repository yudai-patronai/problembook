import os
import random
import shutil

random.seed(42)

def tg(x, y):
    if x == 0:
        if y > 0:
            return float("inf"), "up"
        return - float("inf"), "down"
    elif y == 0:
        if x > 0:
            return 0, "right"
        return 0, "left"
    else:
        return y  / x, x > 0
def generate_test(name, testn):
    n = random.randint(0, 100)
    targets = []
    tarset = set()
    tgs = dict()
    for i in range(n):
        target = random.randint(-100, 100), random.randint(-100, 100)
        while (target in tarset) or (target[0] ** 2 + target[1] ** 2 == 0):
            target = random.randint(-100, 100), random.randint(-100, 100)
        targets.append(target)
        tarset.add(target)
        if tg(target[0], target[1]) in tgs:
            tgs[tg(target[0], target[1])] +=1
        else:
            tgs.update({tg(target[0], target[1]): 1})
        maxx = 0
        for tag in tgs:
             if tgs[tag] > maxx:
                 maxx = tgs[tag]
        ans = maxx
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for nora in targets:
            f.write(str(nora[0])+' '+str(nora[1])+"\n")
    with open(name+".a", "w") as f:
        f.write(str(ans))


def mantest(name,n, targets, ans):
    with open(name, "w") as f:
        f.write(str(n)+"\n")
        for nora in targets:
            f.write(str(nora[0])+' '+str(nora[1])+"\n")
    with open(name+".a", "w") as f:
        f.write(str(ans))




if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
        
    test = 6
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    mantest(test_name, 4, [(2, 2), (4, 4),(-2, -2), (-4, -4)], 2)

    test = 7
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    mantest(test_name, 1, [(1, 1)], 1)

    test = 8
    test_name = os.path.join(test_folder, "%02d" % test)
    print("generating %s..." % test_name)
    mantest(test_name, 2, [(1, 1), (2, 2)], 2)



