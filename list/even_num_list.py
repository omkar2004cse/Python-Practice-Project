a=eval(input("Enter a element of list is:-"))
print("length of is:-",len(a),"list is:-",a)
print("even element in list is:-")
for i in a:
    if i%2==0:
        print(i)
print("odd element in list is:-")
for i in a:
    if i%2!=0:
        print(i)