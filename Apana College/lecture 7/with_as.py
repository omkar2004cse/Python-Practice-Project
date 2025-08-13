with open("demo.txt","r") as f:
    print(f.read())


with open("demo.txt","w") as t:
    t.write("Welcome in Coding")

with open("demo.txt","r") as g:
    print(g.read())