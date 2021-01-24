instructions = []

with open('input.txt') as f:
    instructions = f.read()

# this will read input as a string in python
print("The instructions are read in as a {} in python, with length {}.".format(type(instructions), len(instructions)))

index = 0
for i in instructions:
    if i == '(':
        index = index + 1
    elif i == ')':
        index = index - 1

print("The last position is {}".format(index))