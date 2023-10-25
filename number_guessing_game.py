import random

randomNumber = random.randint(1, 100)
print(randomNumber)

userGusess = None
guesses = 0

while (userGusess != randomNumber):
    userGusess = int(input("Enter the number you guessed: \n"))
    guesses += 1
    if userGusess == randomNumber:
        print("you Gusess the coreect number \n")
    else:
        if userGusess > randomNumber:
            print(
                "You Gusess the wrong number! Please Guess the smaller number \n"
            )
        else:
            if userGusess < randomNumber:
                print(
                    "You Gusess the wrong number! Please Guess the larger number \n"
                )

print(f"You guess the number in {guesses} guesses \n")

if userGusess == randomNumber:
    with open("highscore.txt", 'w') as f:
        f.write(str(userGusess))
