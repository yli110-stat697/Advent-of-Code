boxes = []

with open('input.txt', 'r') as f:
    boxes = f.read().splitlines()

boxes = [list(map(int, box.split('x'))) for box in boxes]


def ribbonLen(ls):
    ls.sort()
    perimeter = 2 * (ls[0] + ls[1])
    cubic = cubic = ls[0] * ls[1] * ls[2]
    return perimeter + cubic


print(sum([ribbonLen(box) for box in boxes]))
