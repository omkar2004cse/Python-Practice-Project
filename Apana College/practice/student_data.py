# input a stuudent data from user and store in list
n=int(input("Enter a Number of student Data Can Stored in list:-"))
li=[]

for i in range(1,n+1):
    li1=[]

    for j in range(1):
        print("student",i,"Data is:-")
        li1.append(input("Name:-"))
        li1.append(int(input("Roll No:-")))
        li1.append(float(input("Total Marks(Percentage):-")))
    li.append(li1)

print(li)