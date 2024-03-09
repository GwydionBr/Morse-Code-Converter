from data import translator

print("Welcome to the Morse-code Converter.")

activated = True
while activated:
    print("\nEnter (1) to convert from Text to Morse-Code."
          "\nEnter (2) to convert from Morse-Code to Text."
          "\nEnter (off) to exit the program.")
    direction = input("Choice: ")


    # Translate Text to Morse-Code
    if direction == "1":
        code = input("Enter code: ")
        answer = ""
        for letter in code:
            morse = translator[letter.lower()]
            answer += morse + " "
        print(f"The Morse code is:\n{answer}")

    # Translate Morse-Code to Text
    elif direction == "2":
        code = input("Enter code: ")
        answer = ""
        new_translator = {translator[k]: k for k in translator}
        new_code = code.split()
        for letter in new_code:
            text = new_translator[letter]
            answer += text
        print(f"The Text is:\n{answer}")

    # Shut down the programm
    elif direction == "off":
        print("Thank you for using the Morse-code Converter")
        activated = False

    # Catching invalid starting_input
    else:
        print("Invalid input. Please try again.")