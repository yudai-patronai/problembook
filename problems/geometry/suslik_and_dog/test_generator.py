import os
import random
import shutil

random.seed(42)


def generate_test(name, testn):
    sus = random.randint(-10000, 10000), random.randint(-10000, 10000)
    dog = random.randint(-10000, 10000), random.randint(-10000, 10000)
    n = random.randint(1, 1000)
    nory = []
    for i in range(n):
        nora = random.randint(-10000, 10000), random.randint(-10000, 10000)
        nory.append(nora)
    flag = False
    for i in range(n):
        suslen = (sus[0]- nory[i][0])**2 + (sus[1]- nory[i][1])**2
        doglen = (dog[0]- nory[i][0])**2 + (dog[1]- nory[i][1])**2
        if suslen * 4 <= doglen:
            flag = True
            ans = i+1
            break
    if not flag:
        ans = -1
    with open(name, "w") as f:
        f.write(str(sus[0])+' '+str(sus[1])+"\n")
        f.write(str(dog[0])+' '+str(dog[1])+"\n")
        f.write(str(n)+"\n")
        for nora in nory:
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
        


