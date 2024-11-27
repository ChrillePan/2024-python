with open ("devices.txt", "a") as file: #Mode a means: Add date to the end of the file without overwrite
    while True:
        new_item = input("Enter device name: ") #Ask the user for a new device name

        if new_item.lower() == "exit": #lower() converts all given input information to lower case
            print("All done!")
            break

        file.write(new_item + "\n") #Add the input to the file plus newline
