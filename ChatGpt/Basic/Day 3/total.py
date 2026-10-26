# Write a program to calculate the total price of five products.
p1=float(input("Enter a Price of 1st Product is:-"))
p2=float(input("Enter a Price of 2nd Product is:-"))
p3=float(input("Enter a Price of 3rd Product is:-"))
p4=float(input("Enter a Price of 4th Product is:-"))
p5=float(input("Enter a Price of 5th Product is:-"))
p=p1+p2+p2+p4+p5
w_gst=(p*18)/100
t_p=p+w_gst
print("Total Price to Pay with GST is:-",t_p)