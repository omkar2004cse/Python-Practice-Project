# Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5
print("Enter a Number of Rows:-")
r=int(input())
for i in range(r+1):
    for j in range(0,i):
        print(i,end=" ")
    print()