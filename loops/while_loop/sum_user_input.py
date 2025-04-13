# if user entered 0 or Negative number then stop the while loop
print("Enter a input:-(when you entered 0 or Negative number then stop)")
j=0
while True:
    i=int(input())
    if i==0 and i<=0:
        break
    j=j+i
print(f"sum is:-{j}")