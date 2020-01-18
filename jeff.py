import random

options = ["rock", "paper", "dildo"]

print("lets play rock, paper, dildo!")
print("what do you choose?")

playermove = input()
if playermove in options:
    print("okay great!")
    print("computers turn...")
    computermove = random.choice(options)
    print("computer chooses " + computermove)
    if playermove == computermove:
        print("its a f*****g draw")
    elif playermove == "paper":
        if computermove == "rock":
            print("you win bitch")
        else:
            print("you lose bitch")
    elif playermove == "rock":
        if computermove == "dildo":
            print("you win bitch")
        else:
            print("you lose bitch")
    elif playermove == "dildo":
        if computermove == "paper":
            print("you win bitch")
        else:
            print("you lose bitch")
else:
    print("invalid input")
