# print number from 1 to 100
print("Number from 1 to 100:-")
for i in range(1,101):
    print(i,end="  ")

# print the number from 100 to 1
print("\nnumber from 100 to 1:-")
for i in range(100,0,-1):
    print(i,end="  ")

# multiplication table 
n=int(input("\nEnter a number:-"))
for i in range(1,11):
    print(n*i)