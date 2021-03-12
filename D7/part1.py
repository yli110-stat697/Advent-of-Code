import numpy as np

wires = []
with open('input.txt', 'r') as f:
    wires = f.read().splitlines()

wires = [wire.split(' -> ') for wire in wires]
wires_keys = [wire[1] for wire in wires]
wires_values = [wire[0].split(' ') for wire in wires]
wires_dict = dict(zip(wires_keys, wires_values))

def Calculate(wire):
    var = None
    if wire[0] == 'NOT':
        var = np.uint16(~ int(wire[1]))
    elif len(wire) == 1:
        var = int(wire[0])
    elif wire[1] == "AND":
        var = int(wire[0]) & int(wire[2])
    elif wire[1] == 'OR':
        var = int(wire[0]) | int(wire[2])
    elif wire[1] == 'LSHIFT':
        var = int(wire[0]) << int(wire[2])
    elif wire[1] == 'RSHIFT':
        var = int(wire[0]) >> int(wire[2])
    return str(var)


def getValue(key):
    wire = wires_dict.get(key)

    if len(wire) == 1:
        if wire[0].isdigit():
            return Calculate(wire)
        else:
            wire[0] = getValue(wire[0])

    elif len(wire) == 2:
        if wire[0] == 'NOT' and wire[1].isdigit():
            return Calculate(wire)
        elif wire[0] == 'NOT' and wire[1].isdigit() == False:
            wire[1] = getValue(wire[1])

    elif len(wire) == 3:
        if wire[0].isdigit() and wire[2].isdigit():
            return Calculate(wire)
        elif wire[0].isdigit() and wire[2].isdigit() == False:
            wire[2] = getValue(wire[2])
        elif wire[0].isdigit() == False and wire[2].isdigit():
            wire[0] = getValue(wire[0])
        elif wire[0].isdigit() == False and wire[2].isdigit() == False:
            wire[0] = getValue(wire[0])
            wire[2] = getValue(wire[2])

    return Calculate(wire)

print("The signal of wire a is {}".format(getValue('a')))