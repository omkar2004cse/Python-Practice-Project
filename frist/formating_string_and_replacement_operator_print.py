# formating 
# syntax is print("formating string %(i OR s OR f)"%(variable list))
a=10
b=54.66
c="string"
print("value of a is %i"%a)
print("value of b is %f and value of c is %s"%(b,c))
# replacement operator
name="ram"
salary=100.33
age=30
print("hello {0}, salary is {1}, age is {2}".format(name,salary,age))
print("a= {x}, b= {y}, c={z}".format(x=a,y=b,z=c)) 