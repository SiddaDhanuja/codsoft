import random
your_input=input("enter the (rck,paper,scissor)")
l=["Rock","Papers","Scissors"]
Computer_choice=random.choice(l)
print(f"\nYou choose {your_input},computer choose {Computer_choice}.\n")
if your_input==Computer_choice:
    print("Both players selected ",your_input,"Both are winners")
elif your_input=="rock":
    if Computer_choice=="Scissors":
        print("Rock beats scissors! You won")
    else:
        print("Paper covers rock! You loose")
elif your_input=="paper":
    if Computer_choice=="rock":
        print("Paper covers rock! You won!")
    else:
        print("Scissors cuts paper! You loose")
elif your_input=="rock":
    if Computer_choice=="Scissors":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
