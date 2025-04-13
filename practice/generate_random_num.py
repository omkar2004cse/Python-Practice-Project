# Generate random
import random
size=int(input("Enter a size of number:-"))
num=['1','2','3','4','5','6','7','9','0']
number=''
for i in range(1,size+1):
    number+=random.choice(num)
print("Random number is:-",number)