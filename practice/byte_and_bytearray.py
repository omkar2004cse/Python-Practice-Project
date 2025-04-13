x=[10,12,13,14]
print(type(x))
b=bytes(x)
# b[2]=12 bytes is immutable
print(type(b))
# print(b) wrong
for i in b:
    print(i)
c=bytearray(x)
# bytesarray is mutable
c[2]=17
print(type(c))
# print(c) wrong
for i in c:
    print(i)

