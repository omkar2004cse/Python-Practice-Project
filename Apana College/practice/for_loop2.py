# search for a number x in this tuple using loop
n=int(input("enter a number:-"))
l=(1,4,9,16,25,36,49,64,81,100)
for el in l:
    if(el == n):
        print("Number is found")
        break
    else:
        continue
