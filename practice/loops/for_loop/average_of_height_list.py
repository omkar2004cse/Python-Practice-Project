size=int(input("Enter a size of list is:-"))
li=[]
total_height=0
print("Enter a Height data")
for i in range(size):
    j=float(input())
    li.append(j)
    total_height=total_height+j
print("List is:-")
print("Average of list is:-",(total_height/size))

