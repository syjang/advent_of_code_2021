

map = [list(line.strip()) for line in open(f'./input.txt', 'r').read().split('\n')]


maxRow = len(map)
maxCol = len(map[0])


def step_right(map):
    sea_cucumber_moved = False
    moved_map = {}

    for i, row in enumerate(map):
        for j, sea_cucumber in enumerate(row):
            if (sea_cucumber != '>'):
                continue
            
            dest_j = (j + 1) % maxCol

            if (map[i][dest_j] == '.'):
                moved_map[(i, j)] = (i, dest_j)
                sea_cucumber_moved = True

    for (si, sj), (ei, ej) in moved_map.items():
        map[si][sj] = '.'
        map[ei][ej] = '>'
    
    return sea_cucumber_moved

def step_down(map):
    sea_cucumber_moved = False
    moved_map = {}

    for i, row in enumerate(map):
        for j, sea_cucumber in enumerate(row):
            if (sea_cucumber != 'v'):
                continue

            dest_i = (i + 1) % maxRow

            if (map[dest_i][j] == '.'):
                moved_map[(i, j)] = (dest_i, j)
                sea_cucumber_moved = True

    for (si, sj), (ei, ej) in moved_map.items():
        map[si][sj] = '.'
        map[ei][ej] = 'v'

    return sea_cucumber_moved

steps = 0
moved_right = moved_down = True

while (moved_right or moved_down):
    steps += 1
    moved_right = step_right(map)
    moved_down = step_down(map)

print(steps)
