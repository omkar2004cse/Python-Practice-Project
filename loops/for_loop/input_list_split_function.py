elment=input("Enter a element of list is:-")
li=elment.split()
print("list is:-",li)
print("type of list is:-",type(li))
len=len(li)
print("length of list is:-",len)
new_list=[]
for i in li:
    j=int(i)
    new_list.append(j)
print("list is:-",new_list)