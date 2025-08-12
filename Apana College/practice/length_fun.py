# Length Function
# Q1
# WAF to print the length of list
def length(l):
    j=0
    for i in l:
        j+=1
    print("Length of List",l," is:-",j)

l=[12,53,23,52,5321,57,2,52,642,522]
length(l)

# Q2  WAF to Print the element of list in single line
def line(l):
    for i in l:
        print(i,end=" ")

line(l)