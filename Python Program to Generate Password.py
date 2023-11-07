
import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)
#Aman Kharwal project..............................................................



#I'm modifying this project to guessing pass project when we have limited options for passwords and we know the options:


print("We found the list of your passwords and we want a certain password among them.")
........