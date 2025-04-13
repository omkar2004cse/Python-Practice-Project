import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#','$',"%","&","(",")","*","+"]
print("Welcome in Password Generator")
n_letter=int(input("How many Letters you want in your password is:-"))
n_number=int(input("How many Number you want in your password is:-"))
n_symbol=int(input("How many Symbol you want in your password is:-"))
password=""
for i in range(1,n_letter+1):
    l_char=random.choice(letter)
    password+=l_char
for i in range(1,n_number+1):
    n_char=random.choice(number)
    password+=n_char
for i in range(1,n_symbol+1):
    s_char=random.choice(symbol)
    password+=s_char
print("Password is:-",password)