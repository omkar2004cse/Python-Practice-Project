age=int(input("Enter a your age:-"))
if age<=12:
    photo=input("You Take Picture (yes/no):-")
    if photo=='yes':
        print("pay 200 Rs")
    else:
        print("pay 150 Rs")
elif age<=18:
    photo=input("You Take Picture (yes/no):-")
    if photo=='yes':
        print("Pay 300 Rs")
    else:
        print("pay 250Rs")
else:
    photo=input("You Take Picture (yes/no):-")
    if photo=='yes':
        print("Pay 500 Rs")
    else:
        print("pay 400 Rs") 