print("Welcome to Python quiz game!")

Playing = input("Do you want to play? ")


if Playing.lower() != "yes":
    print("Thank you.") 
    quit()

print("Okay, Lets play!")
Score = 0

Question1 = input("What does CPU stands for ")
if Question1.lower() == "central processing unit":
    print("correct!")
    Score += 1
else:
    print("Incorrect")

Question2 = input("What does GPU stands for ")
if Question2.lower() == "graphics processing unit":
    print("correct!")
    Score += 1
else:
    print("Incorrect")

Question3 = input("What does RAM stands for ")
if Question3.lower() == "random access memory":
    print("correct!")
    Score += 1
else:
    print("Incorrect")

Question4 = input("What does SSD stands for ")
if Question4.lower() == "solid state drive":
    print("correct!")
    Score += 1
else:
    print("Incorrect")

print("You got " + str(Score) + " questions right.")
print("You got " + str((Score / 4) * 100)  + "%")