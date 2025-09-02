# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5
r=int(input("Enter the number of rows:-"))
for i in range(1,r+1):
    for j in range(i):
        print(i,end=" ")
    print()