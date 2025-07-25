end=int(input("Enter a last Nummber is:-"))
add=0
print("Even number betweeen 1 to",end,"is:-")
for i in range(1,end+1):
    if i%2==0:
        print(i)
        add=add+i
print("addition of even number between 1 to",end,"is:-",add)
