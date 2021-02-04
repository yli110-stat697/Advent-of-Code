boxes = []

with open('input.txt', 'r') as f:
    boxes = f.read().splitlines()

boxes = [list(map(int, box.split('x'))) for box in boxes]


def boxWrap(ls):
    surface = 2 * (ls[0] * ls[2] + ls[0] * ls[1] + ls[1] * ls[2])
    min_surface = min(ls[0] * ls[2], ls[0] * ls[1], ls[1] * ls[2])
    return surface + min_surface


print(sum([boxWrap(box) for box in boxes]))
