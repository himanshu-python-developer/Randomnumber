import random
randNumber = random.randint(1,100)

userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess=int(input("Enter your guess: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You are guess Right Number ")
    else:
        if (userGuess > randNumber ):
            print ("You Guess it wrong! Enter a smaller number")
        else:
            print ("You Guess It Wrong ! Enter A larger NUMBER!")

print(f" You guess the number {guesses} guess")
with open("hiscore.txt","r") as f:
    hiscore = int(f.read())
    
if(guesses<hiscore):
    print("You are just Broken the high score!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))