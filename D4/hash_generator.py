import hashlib
import time

input_str = 'ckczppom'

def hashValueGen():
    i = 1
    while True:
        hash_str = input_str + str(i)
        hash_value = hashlib.md5(hash_str.encode()).hexdigest()
        yield i, hash_value
        i += 1

tic = time.perf_counter()
gen = hashValueGen()
for item in gen:
    if item[1][:6] == '000000':
        print(item)
        break
toc = time.perf_counter()
print("The generator performance is {} seconds".format(toc - tic))