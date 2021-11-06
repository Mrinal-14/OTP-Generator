import random

print("Hello Mam/Sir")

otp=random.randint(00000,10000)


username=input("Please enter your username:")
print("Hiii.... ", username)
print("Your otp is", otp)
password=input("Enter your OTP - ")

if password==str(otp):
    print("Access granted!!! \n Thank you...." , username)
else:
    password!=str(otp)
    print("Access denied!!!\n Try Again")