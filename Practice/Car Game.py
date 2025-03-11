print('''Start - to start the car
Stop - to stop the car
Exit - to exit the game''')
var=input("")
while True:
    if var==("Start"):
        print("Car started... Ready to go!")
        break
    elif var==("Stop"):
        print("Car stopped.")
        break
    elif var==("Exit"):
        break
    else:
        print("I don't understand that...")
        break
