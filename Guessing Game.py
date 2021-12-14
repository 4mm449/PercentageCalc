import random
number = random.randint(1,20)
max_guesses = 10
number_guesses = 0
#print(number)
while number_guesses < max_guesses:
    guess = int(input("What number am I thinking? (between 1 and 20): "))
    if guess > 20 or guess < 1:
        print("Your guess should be within 1 and 20")
        number_guesses -= 1
    elif guess == number:
        print("You have guessed it right in", number_guesses + 1, "tries")
        break
    else:
        print("Wrong, try again")


    number_guesses += 1
print("The number I was thinking of is", number)
