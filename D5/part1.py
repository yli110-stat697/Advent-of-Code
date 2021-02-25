str_input = []
with open('input.txt') as f:
    str_input = f.read().rsplit()

def NumOfVowels(string):
    Vowels = ('a', 'e', 'i', 'o', 'u')
    num = 0
    for s in string:
        if s in Vowels:
            num += 1
    return num

def RepeatedLetter(string):
    i = 0
    while i < len(string) - 1:
        if string[i] == string[i+1]:
            return True
        i += 1
    return False

def ExcludeSubStrings(string):
    substrings = ('ab', 'cd', 'pq', 'xy')
    for s in substrings:
        if s in string:
            return False
    return True

def IsStringNice(string):
    if (NumOfVowels(string) >= 3) & (RepeatedLetter(string)) & (ExcludeSubStrings(string)):
        return 1
    return 0

print(sum(IsStringNice(s) for s in str_input))