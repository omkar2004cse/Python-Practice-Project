# Exercise 6: Display numbers divisible by 5(by list)
l=[]
n=int(input("Enter number of elements:-"))
for i in range(n):
    l.append(int(input()))
print(l)
print("Number is divisible by 5 are from the list is:-")
i=0
while i<n:
    if(l[i]%5==0):
        print(l[i])
    i+=1
