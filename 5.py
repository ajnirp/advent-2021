def parse_point(x):
    # example x: '105,697'
    return tuple(map(int, x.split(',')))

def parse_lines(file_lines):
    result = []
    for file_line in file_lines:
        # example file_line: '105,697 -> 287,697'
        first, second = file_line.strip().split(' -> ')
        result.append((parse_point(first), parse_point(second)))
    return result

def is_horizontal(line):
    first, second = line
    return first[1] == second[1]

def is_vertical(line):
    first, second = line
    return first[0] == second[0]

def min_x(lines):
    return min(min(line[0][0], line[1][0]) for line in lines)

def min_y(lines):
    return min(min(line[0][1], line[1][1]) for line in lines)

def max_x(lines):
    return max(max(line[0][0], line[1][0]) for line in lines)

def max_y(lines):
    return max(max(line[0][1], line[1][1]) for line in lines)

# find slope of a line guaranteed to not be vertical
def slope(line):
    first, second = line
    return (second[1]-first[1])/(second[0]-first[0])

def num_points_with_more_than_1_line(grid, x_range, y_range):
    return sum(grid[x][y] > 1 for x in range(x_range) \
                              for y in range(y_range))

with open('5.txt') as f:
    lines = parse_lines(f.readlines())

# part 1
minx, maxx = min_x(lines), max_x(lines)
miny, maxy = min_y(lines), max_y(lines)

x_range = maxx-minx+1
y_range = maxy-miny+1

grid = [[0 for _ in range(maxy-miny+1)] \
        for _ in range(maxx-minx+1)]

for line in lines:
    first, second = line
    if is_horizontal(line):
        x0, x1, y = first[0], second[0], first[1]
        if x0 > x1:
            x0, x1 = x1, x0
        for x in range(x0, x1+1):
            grid[x-minx][y-miny] += 1
    elif is_vertical(line):
        y0, y1, x = first[1], second[1], first[0]
        if y0 > y1:
            y0, y1 = y1, y0
        for y in range(y0, y1+1):
            grid[x-minx][y-miny] += 1

print(num_points_with_more_than_1_line(grid, x_range, y_range))

# part 2
for line in lines:
    if is_horizontal(line):
        continue
    elif is_vertical(line):
        continue
    slope_ = slope(line)
    (x0, y0), (x1, y1) = line
    if slope_ == 1:
        # rearrange so that x0, y0 is on the left
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        for x in range(x0, x1+1):
            x_ = x-minx
            y_ = y0+(x-x0)-miny
            grid[x_][y_] += 1
    elif slope_ == -1:
        # rearrange so that x0, y0 is on the left
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        for x in range(x0, x1+1):
            x_ = x-minx
            y_ = y0-(x-x0)-miny
            grid[x_][y_] += 1

print(num_points_with_more_than_1_line(grid, x_range, y_range))
