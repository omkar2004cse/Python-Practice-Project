# calculate total mark and grade of student >=90:-'A', 90>mark>=80:-'B', 80>mark>=70:-'C' ,70>mark:-grade'D', 35<mark:-fail
print("Welcome in Grade Calculator");
sub1=int(input("Enter a marathi mark="));
sub2=int(input("Enter a Hindi and sanskrut mark="));
sub3=int(input("Enter a English mark="));
sub4=int(input("Enter a Math's mark="));
sub5=int(input("Enter a Science mark="));
sub6=int(input("Enter a Social Science mark="));
total=sub1+sub2+sub3+sub4+sub5+sub6;
print("Total mark=",total);
grade=(total*100)/600;
print("Percentage :-",grade);
if(grade>=90):
    print("Grade is A");
elif(90>grade>=80):
    print("Grade is B");
elif(80>grade>=70):
    print("Grade is C");
elif(70>grade>=35):
    print("Grade is D");
else:
    print("Fail");