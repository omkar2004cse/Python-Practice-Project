# Email Slicer
email=input("Enter Your Email:-")
index=email.index("@")
username=email[:index]
domain=email[index+1:]
print(f'your username is \"{username}\" and Domain is \"{domain}\"')