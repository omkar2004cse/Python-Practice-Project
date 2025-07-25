size=int(input("Enter a size of list is:-"))
li=[]
print("Enter a Element of List are=")
for i in range(size):
    j=int(input())
    li.append(j)
print("Your List is:-",li)
# print(max(li))
maxum=li[0]
for k in li:
        if maxum<k:
              maxum=k
print("Maximum element from List is:-",maxum)