#In this article, I’ll walk you through how to make a rock, paper, and scissors game with Python. In the rock, paper and
#scissors game our goal is to create a command-line game where a user has the option to choose between rock, paper and
#scissors and if the user wins the score is added, and at the end when the user finishes the game, the score is shown to
#the user.
#To create the Rock, Paper and Scissors game with Python, we need to take the user’s choice and then we need to compare
#it with the computer choice which is taken using the random module in Python from a list of choices, and if the user wins
#then the score will increase by 1:


#import random
#choices = ["Rock", "Paper", "Scissors"]
#computer = random.choice(choices)
#player = False
#cpu_score = 0
#player_score = 0
#while True:
 #   player = input("Rock, Paper or  Scissors?").capitalize()
  #  ## Conditions of Rock,Paper and Scissors
   # if player == computer:
    #    print("Tie!")
    #elif player == "Rock":
     #   if computer == "Paper":
      #      print("You lose!", computer, "covers", player)
       #     cpu_score+=1
        #else:
         #   print("You win!", player, "smashes", computer)
          #  player_score+=1
    #elif player == "Paper":
     #   if computer == "Scissors":
      #      print("You lose!", computer, "cut", player)
       #     cpu_score+=1
        #else:
         #   print("You win!", player, "covers", computer)
          #  player_score+=1
    #elif player == "Scissors":
     #   if computer == "Rock":
      #      print("You lose...", computer, "smashes", player)
       #     cpu_score+=1
        #else:
         #   print("You win!", player, "cut", computer)
          #  player_score+=1
    #elif player=='End':
     #   print("Final Scores:")
      #  print(f"CPU:{cpu_score}")
       # print(f"Player:{player_score}")
        #break

#Creating these types of games will help a beginner to think logically. You can even use this idea to make your own game.
#In the end, creating these types of programs will help you create your algorithms, which is a very important skill for
#coding interviews and competitive programming.

#------Aman Kharwal projects.................

#---------------------------

#----------------------------#another version that I'm modifying:

#I changed the game into some Measuring luck game, and also I notices that in original game computer guesses in one round
#wouldnt change, I tried to fix that problem so I use to put player input first and the coputer random choices went after that.
#and magicaly the original game's problem solved and my new modifying version worked too:


import random
#Student_luck = False

Student_luck = 0
while True:
    print("You must go to class but you dont know about the weather, what would you choose to wear?")
    player = input("Cool clothes, Warm clothes?").capitalize()
    choices = ["Rainy Day", "Sunny Day"]
    computer = random.choice(choices)
    if player == "Warm clothes" and computer == "Rainy Day":
        print(f"You are lucky, You wont catch cold in ", computer, "because of your", player)
        Student_luck+=1
    elif player == "Warm clothes" and computer == "Sunny Day":
        print(f"You are not lucky today, You'll sweat in ", computer, "because of your", player)
        Student_luck-=1
    elif player == "Cool clothes" and computer == "Rainy Day":
        print(f"You are not lucky, You will catch cold in ", computer, "because of your", player)
        Student_luck-=1
    elif player == "Cool clothes" and computer == "Sunny Day":
        print(f"You are lucky today, You wont sweat in ", computer, "because of your", player)
        Student_luck+=1
    elif player=='End':
        print(f"Do you wanna know how lucky you are?")
        print(f"You were lucky:{Student_luck} times")
        break

