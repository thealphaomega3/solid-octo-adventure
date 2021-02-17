while True:
    command = input("> ").lower()
    if command == "start":
        print("Car has started.")
        while True:

            command = input("> ").lower()
            if command == "start":
                print("Car is already started!")

            elif command == "stop":
                print("Car has stopped")
                command = input("> ").lower()
                while command == "stop":
                    print("Car has already stopped.")
                    command = input("> ").lower()




    elif command == "stop":
        print("Start the car first to stop it!")

    elif command == "quit":
        break