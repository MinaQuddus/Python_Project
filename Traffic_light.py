#traffic light
def traffic_light():
    while True:

        light = input ("light (red, yellow, green): ").lower()

        if(light == "red"):
            print("stop")
        elif(light == "yellow"):
            print("look")
        elif(light == "green"):
            print("go")
        else:
            print (light)


        want_countine=input("what to countinue?(y/n) : ").lower()
        if  want_countine != "y":
            print(" Goodbye!")
            break

            
traffic_light()
