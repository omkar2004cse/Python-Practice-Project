size=int(input("Enter a size of list is:-"))
li=[]
for i in range(1,size+1):
    j=(input())
    li.append(j)
print("List is:-",li)
i=0
while i<len(li):
    print(li[i])
    i+=1