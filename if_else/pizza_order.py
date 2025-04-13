print("Welcome in Pizza Town Shop")
print("Pizza Option\n1)Small Pizza is:-100Rs.\n2)Medium Pizza is:-200Rs.\n3)Large pizza is:-300Rs")
select=int(input("Select the option:-"))
if(select==1):
    print("you need Pepperoni for small pizza  (yes/no):-")
    extra=input()
    if extra=='yes':
        price=130
    else:
        price=100
elif(select==2):
    print("you need Pepperoni for Medium pizza  (yes/no):-")
    extra=input()
    if extra=='yes':
        price=250
    else:
        price=200
elif select==3:
    print("you need Pepperoni for Medium pizza  (yes/no):-")
    extra=input()
    if extra=='yes':
        price=350
    else:
        price=300
else:
    print("Invalid input")
print("Your Bill is:-",price)
print("You Order is ready in 10 min.\nThanks.")
