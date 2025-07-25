print("Welcome in Love Calculator")
bf=input("Enter your Male Partner Name is:-")
gf=input("Enter Your Female Paertner Name is:-")
bf=bf.lower()
gf=gf.lower()
t=bf.count("t")
r=bf.count("r")
u=bf.count("u")
e=bf.count("e")
bf_score=t+r+u+e
l=gf.count("l")
o=gf.count("o")
v=gf.count("v")
ee=gf.count("e")
gf_score=l+o+v+ee
love_Score=bf_score+gf_score
print("Your Love Score is:-",love_Score)