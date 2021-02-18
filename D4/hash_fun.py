import hashlib

input_str = 'ckczppom'

def startWithSubstring(substring):
    i = 1
    while True:
        hash_str = input_str + str(i)
        hash_val = hashlib.md5(hash_str.encode()).hexdigest()
        if hash_val[:len(substring)] == substring:
            break
        i += 1
    return i

print(startWithSubstring('00000'))
print(startWithSubstring('000000'))