import random
print("Welcome to Rock,Paper,Scissors game.")
user_choice=int(input("Please select your choice! 0,1,2 for rock,paper and scissors respectively :"))
Cchoice=random.randint(0,2)
if Cchoice==0:
    print("Computer choses Rock")
elif Cchoice==1:
    print("Computer choses Paper")
elif Cchoice==2:
    print("Computer choses Scissors")
if user_choice==0 and Cchoice==1:
    print("You lose!")
elif user_choice==0 and Cchoice==2:
    print("You win!")
elif user_choice==Cchoice:
    print("It's a draw,nobody wins!")
elif user_choice==1 and Cchoice==0:
    print("You win!")
elif user_choice==1 and Cchoice==2:
    print("You lose!")
elif user_choice==2 and Cchoice==0:
    print("You lose!")
elif user_choice==2 and Cchoice==1:
    print("You win!")
else:
    print("Please enter a valid choice!")

