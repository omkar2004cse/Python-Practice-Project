#  Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
row=int(input("Enter a last row number to print is:-"))
for x in range(1,row+1):
    for y in range(1,x+1):
        print(y,end=" ")
    print()