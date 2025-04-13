import random
size=int(input("Enter a Size of random number is:-"))
num=['1','2','3','4','5','6','7','8','9','0']
st=''
for i in range(1,size+1):
    st+=random.choice(num)
print("random number is generated is",st)