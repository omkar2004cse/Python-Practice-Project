f=open("demo.txt","w")
s=f.write("how are you?") 
print(s) #length of string written karte
f.write("Jay shree ram")
f.close()
f=open("demo.txt")
k=f.read()
print(k)
f.close()