with open("practice.txt","r") as f:
    data=f.read()
# replace the java by python
new_data=data.replace("java","python")

with open("practice.txt","w") as f:
    f.write(new_data)

with open("practice.txt") as f:
    d=f.read()

#check learning present in practice file  
print(d.find("learning"))