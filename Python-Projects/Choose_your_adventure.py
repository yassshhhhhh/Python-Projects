name = input("Type your name: ")
print("Welcome", name, "to an unknown adventure!")

answer = input("You got lost in the ninja village, Now you have meet naruto and find a way to home. Type left to go left or type right to right: ").lower()

if answer == "right":
    answer = input("You find to ninja scrolls where one says you have to meet sasuke and other says meet sakura(Sasuke/Sakura): ").lower()
    if answer == "sasuke": 
        print("Sasuke lives in his own world, he ain't helping you find naruto. You Lost!")
    elif answer == "sakura":
        print("Sakura is dumb and also she isn't that usefull for your adventure, You lost!")
    else:
        print("You have typed an incorrect word, Your adventure end here! You will stay in this ninja village forever.")

elif answer == "left":
    answer = input("You found Guy sensei on your way, will you ask him about naruto or not(Yes/No): ").lower()
    if answer == "yes":
        print("You lost, because Guy sensei doesn't remembers anything.")
    elif answer == "no":
        answer = input("Okay, Now you came across hinata, Will you ask her for the help to find naruto(Yes/No): ").lower()
        if answer == "yes":
            print("You chose the correct decision, Hinata will help you to find naruto. You won!")
        elif answer == "no":
            print("You made mistake, You should have asked hinata for help you to find naruto. Now, It's impossible to find naruto. You lose!")
        else:
            print("You have typed an incorrect word, Your adventure end here! You will stay in this ninja village forever.")
    else:
        print("You have typed an incorrect word, Your adventure end here! You will stay in this ninja village forever.")
else:
    print("You have typed an incorrect word, Your adventure end here! You will stay in this ninja village forever.")
