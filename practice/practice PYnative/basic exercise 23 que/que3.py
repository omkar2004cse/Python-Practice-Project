#Exercise 3: Print characters present at an even index number
name=input("Enter a Your name:-")
len_name=len(name)
print("length:-",len_name)
print("Only Even index character is Display")
for x in range(0,len_name):
    if(x%2==0):
        print(name[x])