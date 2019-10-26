def find_person(maze):
    person_pos = None
    for i, row in enumerate(maze):
        if "@" in row:
            person_pos = (i, row.find("@"))
    return person_pos


def no_wall(maze, coord):
    return maze[coord[0]][coord[1]] == ' '


def has_exit(maze):
    person_pos = find_person(maze)
    
    maze_x, maze_y = len(maze)-1, len(maze[0])-1
    check_cell = [person_pos]
    while True:
        #  вышли на границу
        for x, y in check_cell:
            if x in (0, maze_x):
                return True
            elif y in (0, maze_y):
                return True
        
        #  совершаем шаги
        check_new = []
        for x, y in check_cell:
            for coord in [ (x-1, y), (x, y+1), (x+1, y), (x, y-1) ]:
                if no_wall(maze, coord):
                    check_new.append(coord)
            maze[x] = maze[x][:y] + '#' + maze[x][y+1:]
        
        if len(check_new) == 0:
            break
        else:
            check_cell = check_new
    
    return False

height, width = map(int, input().split())
maze = []
for _ in range(height):
    maze.append(input())

print('YES' if has_exit(maze) else 'NO')
