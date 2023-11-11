#Do you think the most complex use of the random module in Python is random sampling? No, we can also generate random
#stories or anything beyond that using the random module. In this article, I’ll walk you through how to create a story
#generator with Python
#Story Generator with Python
#Our task is to generate a random story every time the user runs the program. I will first store the parts of the stories
#in different lists, then the Random module can be used to select the random parts of the story stored in different lists:

#import random
#when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
#who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
#name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
#residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
#went = ['cinema', 'university','seminar', 'school', 'laundry']
#happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
#print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))

#I first imported the random module and then I created parts of the stories in different lists, then I only selected the
#parts of the lists at random to generate a random story.
#As a beginner, you look for creating software applications more, which is not wrong. But spending more time with programs
#which required you to think logically will always help you no matter what aspect of programming interests you.
#Summary
#There are a few areas where the above code could be improved upon, but at a basic level, it meets many secure password
#generation requirements by today’s standards. As a newbie to Python or any other language, you should keep trying these
#types of programs as they help you explore more functions and in the long run will help you design your algorithms and
#doing a great job in coding interviews.

#Aman Kharwal project--------------

#I'm modifying it like this:

#His verb was only for past time, but I change the verbs into future.
#and also I deleted the name list because it was useless.
#---------------harry potter story teller - for fans of harry potter stories--------------
import random
whenn = ['At a certain time', 'When the time comes', 'After the battle of hogwarts', 'After the night voldemort killed harrys parents','some day in the future']
whoo = ['the boy', 'Hermione granger', 'Lord Voldemort', 'Dumbledore', 'Harry potter', 'Dobby the free elf']
residencee = ['Hogwarts','The burrow', 'Number 12 Grimmauld place', 'Godrics hollow' , '4 Privet Drive house']
wentt = ['Hogsmeade', 'Hogshead','ministry of magic', 'cauldron of thought', 'Diagon Alley', 'Ollivanders wand shop', 'Thw quidditch stadium', 'hogwarts library', 'Azkaban prison', 'Forbidden forest', 'hodwarts common room']
happenedd = ['must die','will fight', 'will trust the face in the mirror', 'will save so many lives', 'will sacrifice a lot of memory', ]
print(random.choice(whenn) + ', ' + random.choice(whoo) + ' that lives in ' + random.choice(residencee) + ', will go to the ' + random.choice(wentt) + ' and ' + random.choice(happenedd))


#khob hala dar edameye in majera man mikham juri barname pish bere ke betunim entekhab dashte bashim va dastan haye motefaveti revayat beshe
#ye zare manteghesh taghir mikone vali khob dar nahayat khoruji ke behemun mide kheili jaleb khahad bud
#injuri kam kam mitunim ehtemalan be sakhte ye bazi az noe visual novel nazdik beshim ke man inja say mikonam codesh ro benevisam

