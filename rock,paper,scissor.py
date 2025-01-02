import  random
choices=["rock","paper","scissor"]
user=input("Rock/paper/scissor: ")
print(f"You have selected {user}")
opponent=random.choice(choices)
print(f"AI opponent:{opponent}")
if user=="rock" and opponent=="paper":
    print("Opponent have won")
elif user=="paper" and opponent=="rock":
    print("User have won")
elif  user=="paper" and opponent=="scissor":
    print("opponent have won")
elif user=="scissor" and opponent=="paper":
    print("user have won ")
elif user=="rock" and opponent=="scissor":
    print("User have won")
elif user=="scissor" and opponent=="rock":
    print("opponent  have won")
elif user==opponent:
    print("Draw")
else:
    print("You have typed wrong")