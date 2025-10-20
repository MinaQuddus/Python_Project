def cal():
    while True:

        name=input("what you want?")

        num1=int(input("enter the first number: "))

        num2 = int(input("entry the second number: "))

        if name =="sum":
            print("answer: ",num1+num2)
            
        elif name == "sub":
            print("answer: ", num1-num2)
            
        elif name == "div":
            print("answer: ", num1/num2)
            
        elif name == "mul":
            print("answer:", num1*num2)
         
        else:
            print("is not found")
        


        choice = input("do you want contine ?(y/n): ")
        if choice != "y":
            print("bye")
            break

cal()
