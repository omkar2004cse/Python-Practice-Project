list=eval(input("enter a element of list is:-"))
print("length of list is:-",len(list),"list is:-",list)
i=0
while i<len(list):
    print("element at index",i,"is:-",list[i])
    i=i+1
p=0
for j in list:
    print("element at index",p,"is",j)
    p=p+1
x=len(list)
for k in range(x):
    print("element at index",k,"is",list[k])