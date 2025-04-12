# Swap of two number
frist=int(input("Enter a Frist Number is:-"))
second=int(input("Enter a Second Number is:-"))
print("Before Swap\nFrist=",frist,"Second=",second)


# # thrid variable
# thrid=frist
# frist=second
# second=thrid
# print("After Swap\nFrist:-",frist,"Second:-",second)


# Without thrid variable
frist=frist+second
second=frist-second
frist=frist-second
print("After Swap\nFrist=",frist,"Second:-",second)