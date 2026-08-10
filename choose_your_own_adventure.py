name = input( "what is your name? ")
print("Welcome", name, "to this adventure!")

answer = input ("You are on a dirt road, it has come to an end and you can left or right. Which way you like to go? ").lower()

if answer == "left":
    answer = input ("You come to river, you can walk around or swim accross? Type walk to walk around and swim to across ").lower()

    if answer == "swim":
        print("You swam across and were eaten by alligator. ")

    elif answer =="walk":
        print("You walked for many miles, ran out water and you lost the game")
    
    else:
        print ("No a valid option. You lose! ")

elif answer == "right":
    answer= input("You come to a bridge, it looks wobbly, do you want to cross the bridge or headback?(Cross/back)" ).lower()

    if answer == "back":
        print("You go back and lose! ")

    elif answer =="cross":
        answer= input("You cross the bridge and meet stranger. Do you want talk with them ?(yes/no)").lower()

        if answer=="yes":
            print("You talk to the stranger and they give a gift. You Win!")
            
        elif answer=="no":
            print("You ignore the stranger. You lose!")

        else:
            print("No a valid option. You lose!")
    
    else:
        print (" No a valid option. You lose! ")

else:
    print("Not a valid option. You lose!")

print(" Thank you for trying", name)