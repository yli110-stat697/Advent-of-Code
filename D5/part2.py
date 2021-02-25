from part1 import RepeatedLetter ## side effect is that part1 result got printed out

str_input = []
with open('input.txt') as f:
    str_input = f.read().rsplit()

# imported from part1
# def RepeatedLetter(string):
#     i = 0
#     while i < len(string) - 1:
#         if string[i] == string[i+1]:
#             return True
#         i += 1
#     return False

def DoubleRepeat(string):
    for i in range(len(string)-1):
        sub_str = string[i:i+2]
        remain_str = string[i+2:]
        if sub_str in remain_str:
            return True
    return False

def OneLetterBetween(string):
    sub_odd = string[::2]
    sub_even = string[1::2]
    if RepeatedLetter(sub_even) or RepeatedLetter(sub_odd):
        return True
    return False

def IsStringNice2(string):
    if (DoubleRepeat(string)) & (OneLetterBetween(string)):
        return 1
    return 0

print(sum([IsStringNice2(s) for s in str_input]))