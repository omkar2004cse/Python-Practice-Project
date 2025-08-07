# Check the list is plaindrome not
# li=[1,2,3,4,3,2,1]
li=[1,2,3,4,2,1]
cp=li.copy()
cp.reverse()
if(li==cp):
    print("Plaindrome")
else:
    print("Not Plaindrome")