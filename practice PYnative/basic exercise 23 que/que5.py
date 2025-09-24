# Exercise 5: Check if the first and last numbers of a list are the same
n=int(input("Enter a length of list :-"))
l=[]
for i in range(0,n):
    l.append(int(input()))
print(l)
if(l[0]==l[n-1]):
    print("Frist and last element of list is same")
else:
    print("frist and last element of List is not same")