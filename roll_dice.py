import random

# create a function
def roll_dice():
    min_value = 1
    max_value = 6
    roll= random.randint(min_value, max_value)
    return roll 

# asking how many players want to play?

while True:

    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else:
            print("must be between 2 to 4!")
    else:
        print("Invalid!, try again")

max_score=50
player_scores=[0 for _ in range(players)]

#main 

while max(player_scores) < max_score:
    for i in range(players):
        print("\nPlayer", i+1, "turn has just started!")
        print("Your total score is:", player_scores[i],"\n")
        current_score = 0

        while True:   
            should_roll = input("would you like to roll (y)?: ")
            if should_roll.lower() != "y":
                break

            value=roll_dice()

            if value == 1:
                print("Yo rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:",value)

            print("Your score is:", current_score)
    
        player_scores[i] += current_score
        print("Your total score is: ", player_scores[i])

max_score = max (player_scroes)
winnng_inx = player_scores.index(max_score)
print("player number", winnng_inx+1, "is the winner with a score of:", max_score)



        
    