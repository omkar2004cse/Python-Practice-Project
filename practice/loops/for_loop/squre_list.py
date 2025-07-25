lsize=int(input("Enter a Size of List:-"))
li=[]
for i in range(lsize):
    j=int(input())
    li.append(j)
print("List is:-",li)
list=[]
for i in li:
    squre=i**2;
    print(squre)
    list.append(squre)
print("Squre list is:-",list)
print("Type is:-",type(list))