# create account class with 2 attributes blance & account no.create function debit,credit,blance
class account:
    def __init__(self,acc_no,blance):
        self.acc_no=acc_no
        self.blance=blance
    def debit(self,amount):
        self.blance-=amount
        print(amount,"is debit sucessful from your account",self.acc_no,"\nAccount Blance is:-",self.blance)
    def credit(self,amount):
        self.blance+=amount
        print(amount,"is Creadited sucessful in your account",self.acc_no,"\nAccount Blance is:-",self.blance)
    def bl(self):
        print("Acc No:-",self.acc_no,"& Bank Blance is",self.blance)
print("Welcome in ABC Bank")
acc=(input("Enter a your 10 digit Account No(hint-7822889258):-"))
o=account(acc,50000)
if(acc=="7822889258"):
    print("Hello..Omkar\nWelcome in ABC Bank")
    print("Your Account No is:-",o.acc_no,"\nYour Bank Blance is:-",o.blance)
    print("**Which Transaction Perfrom in Your Account**\n1)debit\n2)credit\n3)Account Blance")
    i=int(input("Enter a input:-"))
    if(i==1):
        am=int(input("Enter a Amount to Withdraw from Your Account:-"))
        o.debit(am)
    elif(i==2):
        am=int(input("Enter a Amount to Add in Your Account:-"))
        o.credit(am)
    elif(i==3):
        o.bl()
    else:
        print("Please select valid input..\nThank You")
else:
    print("Please check your Account number")
