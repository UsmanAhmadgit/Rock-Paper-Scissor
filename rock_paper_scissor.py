'''                         Rock Paper Scissor Game
rock = 0
paper = 1
scissor = 2
'''
import random
computer = random.choice([0,1,2])
user_choice = input("Enter your choice:\n'r' for rock\n'p' for paper\n's' for scissor\n")
dict={"r":0,"p":1,"s":2}
reversedict={0:"rock",1:"paper",2:"scissor"}
if (user_choice not in dict):
    print("You have entered wrong choice")
else:
    user=dict[user_choice]
    print(f"You chose {reversedict[user]} and Computer chose {reversedict[computer]}")
    if(computer==user):
        print("The game is drawn")
    else:
        if(computer==0 and user==1):
            print("You Win!")
        elif(computer==0 and user==2):
            print("You Lose!")
        elif(computer==1 and user==0):
            print("You Lose!")
        elif(computer==1 and user==2):
            print("You Win!")
        elif(computer==2 and user==0):
            print("You Win!")
        elif(computer==2 and user==1):
            print("You Lose!")

