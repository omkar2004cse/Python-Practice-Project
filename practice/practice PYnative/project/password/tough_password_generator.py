import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#','$',"%","&","(",")","*","+"]
print("Welcome in Password Generator")
n=int(input("Enter a how many Number in password is:-"))
l=int(input("Enter a how many Letter in password is:-"))
s=int(input("Enter a how many Symbol in password is:-"))
# pas="" string cha jagi list ghene for strong password generator
pas=[]
for i in range(1,n+1):
    n_char=random.choice(number)
    pas+=n_char
for j in range(1,l+1):
        l_char=random.choice(letter)
        pas+=l_char
for k in range(1,s+1):
            s_char=random.choice(symbol)
            pas+=s_char
print("Password is:-",pas)
random.shuffle(pas)
print("Shuffle password is:-",pas)
strong_pass=""
for i in pas:
        strong_pass+=i
print("Strong password is:-",strong_pass)