#An acronym is a short form of a word created by long words or phrases such as NLP for natural language processing.
# In this article, I will walk you through how to write a program to create acronyms using Python.
#To create acronyms using Python, you need to write a python program that generates a short form of a word from a given
# sentence. You can do this by splitting and indexing to get the first word and then combine it. Let’s see how to create
# an acronym using Python:
user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
#In the above code, I am first taking a string user input, then I am using the split() function in Python for splitting
# the sentence. Then I declared a new variable ‘a’ to store the acronym of a phrase.
#Then at the end, I am running a for loop over the variable ‘text’ which represents the split of user input. While
# running the for loop we are storing the index value of str[0] of every word after a split and turning it into an
# uppercase format by using the upper() function.

#Summary
#This is a great python program to test your logical skills. These types of programs contribute a lot to your coding
# interviews. So you should keep trying such programs to develop a good understanding of creating algorithms to perform
# well in your coding interviews.

#I hope you liked this article on how to create acronyms with the Python programming language. Feel free to ask your
# valuable questions in the comments section below.

#Aman Kharwal project--------------

#I Modified this project to this one:

user_input = str(input("Enter your phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(f"The Acronyms of your phrase is: {a}")
