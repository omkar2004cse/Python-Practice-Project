size=int(input("Enter a size of row:-"))
print("Right angled triangle is:-")
for i in range(size+1):
    for j in range(i):
        print("*",end=" ")
    print()