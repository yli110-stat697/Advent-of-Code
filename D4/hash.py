import hashlib

input_str = 'ckczppom'

i = 1
while True:
    hash_str = input_str + str(i)
    hash_val = hashlib.md5(hash_str.encode()).hexdigest()
    if hash_val[:5] == '00000':
        print("The number that produces five zeros hash value is {}.".format(i))
        print("The hash value is {}.".format(hash_val))
        print("The concatenated string is {}.".format(hash_str))
        break
    i += 1