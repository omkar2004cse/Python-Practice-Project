# Write a Python code to display numbers from a list divisible by 5
# Given list is  [10, 20, 33, 46, 55]
li=[10, 20, 33, 46, 55]
for i in range(len(li)):
    if(li[i]%5==0):
        print(li[i])
    else:
        continue