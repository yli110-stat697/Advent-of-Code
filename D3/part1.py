directions = []
with open('input.txt', 'r') as f:
    directions = f.read()

i = 0
j = 0
position = (i, j)
positions = set()
positions.add(position)

for direction in directions:
    if direction == '>':
        j += 1
    elif direction == '<':
        j -= 1
    elif direction == '^':
        i -= 1
    elif direction == 'v':
        i += 1
    else:
        raise Exception("Direction is not clear!")
    position = (i, j)
    positions.add(position)

print("The number of houses visited are {}.".format(len(positions)))