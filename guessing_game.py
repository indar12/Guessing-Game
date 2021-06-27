from random import randint

start = int(input("Start bound: "))

end = int(input("End bound: "))

guess_answer = randint(start, end)

while True:
    try:
        guess = int(input('Guess the number between {0} and {1}: '.format(start,end)))
        if start <= guess <=end:
            if guess == guess_answer:
                print("You Won!!!")
                break
            else:
                 print("You lost!!! Try again")
                 continue
        else:
            print("Enter your guess between {0} and {1}".format(start,end))
    except ValueError:
        print("Please enter a number")
        continue
