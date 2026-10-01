import random

number = random.randint(1, 100)

for i in range(5):
    guess = int(input("Guess the number: "))
    if guess==number:
        print("correct")
        break
    
    elif guess < number:
        if i==4:
            break
        print("guess bigger")

    elif guess>number :
        if i==4:
            break
        print("guess smaller")

        