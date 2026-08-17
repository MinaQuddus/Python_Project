# random generat math question
import random
import time

OPERATOR = ["+","-","*"]
MIN_OPERATOR =3
MAX_OPERATOR=12
TOTAL_PROBLEM = 10

def generator_problem():
    left = random.randint(MIN_OPERATOR, MAX_OPERATOR)
    right = random.randint (MIN_OPERATOR, MAX_OPERATOR)
    oporator = random.choice(OPERATOR )

    expr= str(left) + " "+ oporator+ " "+ str(right)
    answer =eval (expr)
    return expr,answer

wrong = 0
# ask the question

input(" Press enter to start!")
print("-----------------------")

start_time=time.time()


for i in range(TOTAL_PROBLEM):
    expr,answer = generator_problem()
    while True:
        guess = input ("problem #" + str(i+1)+ ": "+ expr+ " = ")
        if guess == str(answer):
            break
        wrong+=1

end_time=time.time()
total_time=round(end_time-start_time,2)

print("-----------------------")
print(f"Nice work! {total_time} seconds")


    






 