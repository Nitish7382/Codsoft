import random

def computer():
    return random.choice(["rock","paper","scissor"])

def player():
    while True:
        playerInput = input("Enter your choice(rock,paper,siccors) : ")
        if playerInput in ['rock','paper','scissor'] :
            return playerInput
        else:
            print("invalid input! Please input again")

def winner(user,system):
    if user == system:
        return "Its a Tie!"
    elif (user == 'rock' and system == 'scissor') or\
         (user =="paper" and system == "rock") or\
         (user == "scissor" and system =="paper"):
        return "You Won!"
    else:
        return "You Lost!"
    
def getResult(user,system,result):
    print("you Chose: ",user)
    print("Computer chose: ",system)
    print(result)

def playAgain():
    while True:
        again = input("Do you want to play again(y/n): ")
        if again in ["y","n"]:
            return again == "y"
        else:
            print("Enter a valid response!")

def main():
    userScore = 0
    systemScore = 0

    while True:
        user = player()
        system = computer()
        result = winner(user,system)
        getResult(user,system,result)

        if result == "You Won!":
            userScore +=1
        elif result == "You Lost!":
            systemScore +=1

        print(f"you score: {userScore}, Computer score: {systemScore}")

        if not playAgain():
            print("Thanks for playing")
            break;   

if __name__ == "__main__":
    main()