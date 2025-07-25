size=int(input("Enter a Size of List:-"))
li=[]
for i in range(size):
    j=int(input())
    li.append(j)
print("List is:-",li,"\ntype is:-",type(li),"\nlength of list is:-",len(li))
remove=int(input("Enter a number is remove form list:-"))
new_list=[]
for k in li:
    if(k==remove):
        continue
    else:
        new_list.append(k)
print("New list is:-",new_list)
print("Length of list is:-",len(new_list))