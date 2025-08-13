# Write a recursive function to print all element in a list (use list & index as parameter)
def element(p,i=0):
    # for i in range(len(p)):
    #     print(p[i])
    if(i==len(p)):
        return
    print(p[i])
    element(p,i+1)


s=int(input("enter a Size of list:-"))
l=[]
print("enter a",s,"Element of list")
for i in range(s):
    print(i,end="-")
    l.append(int(input("")))
print(l)
element(l)