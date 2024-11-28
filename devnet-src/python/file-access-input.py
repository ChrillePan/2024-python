print(f"Add your device via user input. Leave the program with 'exit'") #Program info

with open ("devices.txt", "a") as file: #Mode a means: Add data to the end of the file without overwrite
    while True:
        new_item = input("Enter device name: ") #Ask the user for a new device name

        if new_item.lower() == "exit": #lower() converts all given input information to lower case
            print("All done!")
            break

        else:
            file.write(new_item + "\n") #Add the input to the file plus newline
