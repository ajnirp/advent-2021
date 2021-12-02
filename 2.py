commands = []

horiz = 0
depth = 0

with open('2.txt') as f:
    for line in (x.strip() for x in f):
        val = int(line.split()[1])
        command = line[0]
        if command == 'f':
            horiz += val
        elif command == 'u':
            depth -= val
        else:
            depth += val
        commands.append((command, val))

print(horiz * depth)

aim = 0
horiz = 0
depth = 0
for pair in commands:
    command, val = pair
    if command == 'f':
        horiz += val
        depth += aim * val
    elif command == 'u':
        aim -= val
    else:
        aim += val

print(horiz * depth)
