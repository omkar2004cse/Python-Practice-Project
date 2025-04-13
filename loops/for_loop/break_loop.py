size=int(input("Enter a Size of List is:-"))
li=[]
print("If Entered number greater than 45 then stop input:-")
for i in range(size):
    j=int(input())
    if j>=45:
          break
    else:
        li.append(j)
print("list is:-",li)