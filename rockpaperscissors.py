#Rock paper scissors game

import random
choices = ["rock","paper","scissors"]

while True :
   
    computer = random.choice(choices).lower()
    user = input("rock , paper , or scissors :").strip().lower()

    if user not in choices :
        print("invalid choice")
        continue   #so that is goes back to start of the loop instead of printing do u wann play again

    print("computer :",computer)
    print("user : " , user )
    
    if user == computer :
        print("its a tie !")

    elif(user == "rock" and computer == "scissors"  or \
         user == "paper" and computer == "rock" or \
         user == "scissors" and computer =="paper"):
        print("you win !")
    else :
        print("You lose")
        
    play_again = input("Do u wanna play again?(yes/no) :").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
     
    