# WAF to convert USD to INR
def inr(p):
    r=p*87.63
    print(p,"USD=",r,"INR")

n=float(input("Enter a Dollar:-"))
inr(n)