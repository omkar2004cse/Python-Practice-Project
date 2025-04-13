frist=int(input("Enter a Frist number is:-"))
second=int(input("Enter a Second number is:-"))
print("Before swap")
print("Frist=",frist,"Second=",second)
# # by thrid variable
# third=frist
# frist=second
# second=third
# print("After Swap\nFrist=",frist,"Second=",second)
frist=frist+second
second=frist-second
frist=frist-second
print("After Swap\nFrist=",frist,"Second=",second)