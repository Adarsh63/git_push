# my_script.py

def process_input(input_code):
    # Your logic to process the input code goes here
    result = f"Processed: {input_code}"
    return result


if __name__ == "__main__":
    while True:
        # Read input from an external file or command-line argument
        try:
            with open("input.txt", "r") as file:
                input_code = file.read().strip()
        except FileNotFoundError:
            #input_code = input("Enter code (press Ctrl+D on a new line to finish):\n\n\n        ")
            # Start with an empty string
            input_code = ''

            # Prompt the user to enter code line by line
            print("Enter code (press Enter twice to finish):")
            while True:
                line = input()
                if not line:
                    break
                input_code += line + '\n'

        # Process the input
        output = process_input(input_code)

        # Display or save the result
        print(output)

        # Update the script with the input code and formatted output
        formatted_output = '"""\n' + output + '\n"""'
        with open(__file__, "a") as script_file:
            script_file.write(f'\n{formatted_output}\n')

        # Optionally, update an external file with the result
        with open("output.txt", "a") as file:
            file.write(output + "\n")

        # Ask the user if they want to continue
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            break

