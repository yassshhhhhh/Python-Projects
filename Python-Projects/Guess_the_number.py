import random


intro = print("Lets play!")
top_range = input("Type any number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()

ran_ans = random.randint(0, top_range)
#print(ran_ans)
guesses = 0

while True:
    guesses += 1
    guess = input("Enter your guess? ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please type a number next time.")
        continue

    if guess == ran_ans:
        print("You got it!")
        break
    elif guess < ran_ans:
        print("It's aboveeee")
    else:
        print("It's belowwww")

print("You got the correct number in", guesses, "guesse(s).")
