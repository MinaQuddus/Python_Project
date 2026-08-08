print("Welcome to my computer quiz!")


playing = input("Do you want to play? ")


if playing.lower()!= "yes":
    quit()


print ("let's play!" )
score=0


answer = input("what does RAM stand for? ").lower()


if answer== "ramdom access memory":
    print('correct!')
    score=+1
else:
    print('incorrect!')


answer = input("what does PSU stand for? ")


if answer == "power supply":
    print('correct!')
    score=+1
else:
    print('incorrect!')


answer = input("what does GPU stand for? ")


if answer == "graphics processing unit":
    print('correct!')
    score=+1
else:
    print('incorrect!')


print(" you got " + str(score) + " question  correct!")
