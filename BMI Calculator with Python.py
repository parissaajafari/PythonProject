#The Body Mass Index or BMI is calculated from weight and height of a Person. In this article, I will walk you through
#how to create a BMI calculator with Python.
#What is Body Mass Index (BMI)?
#BMI is a measure of relative weight based on an individual’s mass and height. Today, Body Mass Index is commonly used to
#classify people as underweight, overweight, and even with obesity. Also, it is adopted by countries to promote healthy eating.
#BMI can be considered as an alternative for direct measurements of body fat. Besides, BMI is an inexpensive and easy-to-perform
# method of screening for weight classes that may cause health problems.

#BMI Calculator with Python
#The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters, then dividing
#the answer again by their height. Now let’s see how to create a BMI calculator with Python:

#Height=float(input("Enter your height in centimeters: "))
#Weight=float(input("Enter your Weight in Kg: "))
#Height = Height/100
#BMI=Weight/(Height*Height)
#print("your Body Mass Index is: ",BMI)
#if(BMI>0):
#	if(BMI<=16):
#		print("you are severely underweight")
#	elif(BMI<=18.5):
#		print("you are underweight")
#	elif(BMI<=25):
#		print("you are Healthy")
#	elif(BMI<=30):
#		print("you are overweight")
#	else: print("you are severely overweight")
#else:("enter valid details")

#I hope you liked this article on how to calculate Body Mass Index/BMI with Python programming language.

#----------------------------Aman Kharwal
#------------------
#------------

#Now I'm modifying Project for Calculating BMR & Daily calorie intake for each person:

Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your Weight in Kg: "))
Age = int(input("Enter your Age: "))
Gender = str(input("Enter your Gender: ")).lower()

print("1-Sedentary(never exercised)",
	  "2-Somewhat active(moderate activity 3-5 times a week)",
	  "3-very active(vigorous exercise 5-6 days a week)",
	  "4-extremely active(professional athleth)")
Activity=str(input("Enter yout acivity level between 1 to 4: "))
if Gender == 'male':
    if Activity == '1':
        BMR = (10 * Weight) + (6.25 * Height) - (5 * Age) + 5
        Calorie = BMR*1.1
        print("your Basal Metabolic Rate is:", BMR)
        print("Your daily calorie intake is:", Calorie)
    elif Activity == '2':
        BMR = (10 * Weight) + (6.25 * Height) - (5 * Age) + 5
        Calorie = BMR*1.2
        print("your Basal Metabolic Rate is:", BMR)
        print("Your daily calorie intake is:", Calorie)
    elif Activity == '3':
        BMR= (10*Weight)+(6.25*Height)-(5*Age)+5
        Calorie = BMR*1.3
        print("your Basal Metabolic Rate is:", BMR)
        print("Your daily calorie intake is:", Calorie)
    elif Activity == '4':
        BMR = (10*Weight)+(6.25*Height)-(5*Age)+5
        Calorie = BMR*1.4
        print("your Basal Metabolic Rate is:", BMR)
        print("Your daily calorie intake is:", Calorie)
    else:
        print("please insert your activity level between number 1 to 4: ")
        print("1-Sedentary(never exercised)","2-Somewhat  active(moderate activity 3-5 times a week)","3-very active(vigorous exercise 5-6 days a week)","4-extremely active(professional athleth)")

elif Gender == 'female':
    BMR = (10 * Weight) + (6.25 * Height) - (5 * Age) -161
    if Activity == '1':
        Calorie = BMR*1.1
        print("your Basal Metabolic Rate is:", BMR)
        print("Your daily calorie intake is:", Calorie)
    elif Activity == '2':
        Calorie = BMR*1.2
        print("your Basal Metabolic Rate is:", BMR)
        print("Your daily calorie intake is:", Calorie)
    elif Activity == '3':
        Calorie = BMR*1.3
        print("your Basal Metabolic Rate is:", BMR)
        print("Your daily calorie intake is:", Calorie)
    elif Activity == '4':
        Calorie = BMR*1.4
        print("your Basal Metabolic Rate is:", BMR)
        print("Your daily calorie intake is:", Calorie)
    else:
        print("please insert your activity level between number 1 to 4: ")
        print("1-Sedentary(never exercised)","2-Somewhat active(moderate activity 3-5 times a week)","3-very active(vigorous exercise 5-6 days a week)","4-extremely active(professional athleth)")
else:
    print("Plese choose your gender between male or female: ")


