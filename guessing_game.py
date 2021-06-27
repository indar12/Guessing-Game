import random
import sys
generate = random.randint(int(sys.argv[1]), int(sys.argv[2]))
while True:
    try:
        guess = int(input("Guess the number 1 to 10: "))
        if 0 < guess < 11:
            if guess == generate:
                print("You are correct!!!")
                break
        else:
            print("Enter a number between 1 to 10")
    except ValueError:
        print("Please enter a number")
        continue
