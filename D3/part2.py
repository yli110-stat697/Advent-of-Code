directions = []

with open('input.txt', 'r') as f:
    directions = f.read()

santa = directions[::2]
robo = directions[1::2]

def GetHouses(directions):
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
        elif direction == 'v':
            i += 1
        elif direction == '^':
            i -= 1
        else:
            raise Exception("Directions not clear!")
        position = (i,j)
        positions.add(position)
    return positions

print(len(GetHouses(santa) | GetHouses(robo)))