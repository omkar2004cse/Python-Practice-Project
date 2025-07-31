# input five subject mark out of 100 and calculate the grade 
print("\"Enter a your subject mark\"")
s1=int(input("Marathi:-"))
s2=int(input("English:-"))
s3=int(input("Hindi:-"))
s4=int(input("Maths:-"))
s5=int(input("Science:-"))
total=s1+s2+s3+s4+s5
print("Total mark obtained is:-",total)
avg=total/5
print("Average is:-",avg)
if(avg>=75):
    print("Grade is:-\"A\"")
elif(avg<75 and avg>=60):
    print("Grade is:-\"b\"")
elif(avg>=35 and avg<60):
    print("Grade is:-\"c\"")
else:
    print("Grade is:-\"Fail\"")