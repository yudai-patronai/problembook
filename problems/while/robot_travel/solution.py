def travel():
    x, y = input().split()
    x, y = int(x), int(y)
    cmd = input()

    while cmd != "stop":
        direction, step = cmd.split()
        step = int(step)

        if direction == "left":
            x -= step
        elif direction == "top":
            y += step
        elif direction == "right":
            x += step
        elif direction == "down":
            y -= step
        else:
            #  можно осложнить задачу и дать проверку корректности ввода команды
            pass

        cmd = input()

    return x, y

print(*travel())