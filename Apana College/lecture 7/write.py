f=open("demo.txt","w")
s=f.write("don omkar") 
print(s) #length of string written karte
f.close()
f=open("demo.txt")
k=f.read()
print(k)
f.close()