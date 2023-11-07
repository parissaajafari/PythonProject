#Most countries around the world use the Celsius scale to indicate temperatures, but the United States still uses the
#Fahrenheit scale. In this article, I will take you through a very simple program for beginners to convert Fahrenheit to
#celsius with Python programming language.
#Python Program To Convert Fahrenheit to Celsius:
#Calculating temperature conversion is simple. We have to convert the temperature because Celsius and Fahrenheit have
#different starting points; 0 degrees Celsius is 32 degrees Fahrenheit. So to convert Fahrenheit to degrees Celsius, we
#just need to subtract 32 from the temperature Fahrenheit.

#Sometimes the size of the units is also different. Celsius divides the temperature range between the freezing and boiling
#points of water is 100 degrees, while Fahrenheit divides this range into 180 degrees, so I will also multiply the value
#by 5/9 to convert 180 degrees into 100.

#Let’s see how to do this with Python:

#def convert(s):
 #   f = float(s)
  #  c = (f - 32) * 5/9
   # return c

#print(convert(78))

#So this is how we can convert temperatures with Python programming language.

#-----------------Aman Kharwal Projects

#----How to convert cantigrad to kelvin
def convert(s):
    c = float(s)
    k = (c + 273)
    return k
c=input("Centigrade to Kelvin? just write the Temperature:")
k=convert(float(c))
print("The temperature is", k ,"°K")


def convert(s):
    k = float(s)
    c = (k - 273)
    return c
k=input("Kelvin to Centigrade? just write the Temperature:")
c=convert(float(c))
print("The temperature is", c ,"°C")

