# print the element of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
n=int(input("Enter a Nth number:-"))
a=1
l=[]
while a<=n:
    l.append(a**2)
    a+=1
print(l)