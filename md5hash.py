import hashlib
result = hashlib.md5(b'Suraj')
print("The byte equivalent of hash is: ", end ="")
print(result.digest())
