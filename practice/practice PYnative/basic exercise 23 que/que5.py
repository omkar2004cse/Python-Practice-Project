# Exercise 5: Check if the first and last numbers of a list are the same
li=[]
s=int(input("Enter a Size of List-"))
print("Enter a element of list is:-")
for i in range(s):
    print((i+1),"element is:-")
    e=int(input())
    li.append(e)
# print(li)
if(li[0]==li[s-1]):
    print("list frist and Last Element is same:-",li)
else:
    print("Frist and Last Element of List is not Same:-",li)