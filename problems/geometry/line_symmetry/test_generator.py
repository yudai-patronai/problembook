import os
import random
import shutil

random.seed(42)
def hor_test(name, testn):
    xa = random.randint(-1000, 1000)
    ya = random.randint(-1000, 1000)
    x1 = random.randint(-1000, 1000)
    x2 = random.randint(-1000, 1000)
    y1 = random.randint(-1000, 1000)
    y2 = y1

    xb = xa
    yb = 2 * y1 - ya
    ans  = str(xb)+' '+str(yb) 

    with open(name, "w") as f:
        f.write(str(x1)+' '+str(y1)+" ")
        f.write(str(x2)+' '+str(y2)+"\n")
        f.write(str(xa)+' '+str(ya)+"\n")

    with open(name+".a", "w") as f:
        f.write(ans)
     
def ver_test(name, testn):
    xa = random.randint(-1000, 1000)
    ya = random.randint(-1000, 1000)
    y1 = random.randint(-1000, 1000)
    y2 = random.randint(-1000, 1000)
    x1 = random.randint(-1000, 1000)
    x2 = x1

    xb = 2 * x1 - xa
    yb = ya
    ans  = str(xb)+' '+str(yb) 

    with open(name, "w") as f:
        f.write(str(x1)+' '+str(y1)+" ")
        f.write(str(x2)+' '+str(y2)+"\n")
        f.write(str(xa)+' '+str(ya)+"\n")

    with open(name+".a", "w") as f:
        f.write(ans)



def generate_test(name, testn):
    k = random.randint(1, 10000)
    sign  = 2 * random.randint(0, 2) - 1
    k *= sign
    b = random.randint(-1000, 1000)
    x1 = random.randint(-1000, 1000)
    x2 = random.randint(-1000, 1000)
    y1 = k * x1 + b
    y2 = k * x2 + b
    
    xa = random.randint(-1000, 1000)
    ya = random.randint(-1000, 1000)
    
    k_perp = 1 / k
    b_perp = ya- k_perp * xa
    inter_x = (b_perp - b) / (k - k_perp)
    inter_y = k * inter_x + b
    xb = 2 * inter_x - xa
    yb = 2 * inter_y - ya
    
    ans  = str(xb)+' '+str(yb) 
    with open(name, "w") as f:
        f.write(str(x1)+' '+str(y1)+" ")
        f.write(str(x2)+' '+str(y2)+"\n")
        f.write(str(xa)+' '+str(ya)+"\n")

    with open(name+".a", "w") as f:
        f.write(ans)
            



if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    for test in range(1, 6):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        generate_test(test_name, test)
    for test in range(6, 8):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        hor_test(test_name, test)
        
    for test in range(8, 10):
        test_name = os.path.join(test_folder, "%02d" % test)
        print("generating %s..." % test_name)
        ver_test(test_name, test) 
