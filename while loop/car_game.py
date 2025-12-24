command = ""

while True:
    command = input("> ").lower()

    if(command == "help"):
        print("""
start - To start the car
stop - To stop the car
quit - To quit
""")
        
    elif(command == "start"):
        print("Car started")

    elif(command == "stop"):
        print("Car stopped")

    elif(command == "quit"):
        break

    else:
        print("Sorry, I did not understand that")                

            