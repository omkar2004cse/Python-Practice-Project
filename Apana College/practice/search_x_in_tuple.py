# search for a number x in tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]
l=[1,4,9,16,25,36,49,64,81,100]
print(l)
print(type(l))
t=tuple(l)
print(t)
print(type(t))
x=int(input("Enter a number:-"))
i=1
# n=1
# while i<len(t):
#     if(t[i]==x):
#         n=t[i]
#     i+=1
# if(n==x):
#     print("Number is Present")
# else:
#     print("Number is not Present")


# using the break and continue keyword 
while i < len(t):
    if(t[i]==x):
        print("Number is Found at index",i)
        break
    else:
        i+=1
        continue
        