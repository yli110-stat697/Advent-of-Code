instructions = []
with open('input.txt') as f:
    instructions = f.read()

floor = 0
position = 0
while position < len(instructions):
    if instructions[position] == '(':
        floor = floor + 1
    elif instructions[position] == ')':
        floor = floor - 1
    position += 1
    if floor == -1:
        print("The first time to enter basement is at position {}".format(position))
        break