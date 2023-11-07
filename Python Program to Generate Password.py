
import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)
#Aman Kharwal project..............................................................



#I'm modifying this project to guessing pass project when we have limited options for passwords and we know the options:


print("We found the list of your passwords and we want a certain password among them.")
Password = input("Enter first name of your password: ").strip()

user_input = str(input("Enter a list of your passwords: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
    if a == 'password':
        print(f"we found your password. your password is{a}")
