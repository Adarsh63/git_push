# # my_script.py
#
# def process_input(input_code):
#     # Your logic to process the input code goes here
#     result = f"Processed: {input_code}"
#     return result
#
#
# if __name__ == "__main__":
#     while True:
#         # Read input from an external file or command-line argument
#         try:
#             with open("input.txt", "r") as file:
#                 input_code = file.read().strip()
#         except FileNotFoundError:
#             #input_code = input("Enter code (press Ctrl+D on a new line to finish):\n\n\n        ")
#             # Start with an empty string
#             input_code = ''
#
#             # Prompt the user to enter code line by line
#             print("Enter code (press Enter twice to finish):")
#             while True:
#                 line = input()
#                 if not line:
#                     break
#                 input_code += line + '\n'
#
#         # Process the input
#         output = process_input(input_code)
#
#         # Display or save the result
#         print(output)
#
#         # Update the script with the input code and formatted output
#         formatted_output = '"""\n' + output + '\n"""'
#         with open(__file__, "a") as script_file:
#             script_file.write(f'\n{formatted_output}\n')
#
#         # Optionally, update an external file with the result
#         with open("output.txt", "a") as file:
#             file.write(output + "\n")
#
#         # Ask the user if they want to continue
#         choice = input("Do you want to continue? (yes/no): ").lower()
#         if choice != 'yes':
#             break
#
#
# """
# Processed:         # Ask the user if they want to continue
#         choice = input("Do you want to continue? (yes/no): ").lower()
#         if choice != 'yes':
#             break
#
# """
import subprocess


def process_input(input_code):
    # Your logic to process the input code goes here
    result = f"Processed: {input_code}"
    return result

def git_commit_and_push(message="Auto commit", branch="main"):
    try:
        # Add all changes to the staging area
        subprocess.run(["git", "add", "."], check=True)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", message], check=True)

        # Push changes to the remote repository
        subprocess.run(["git", "push", "origin", branch], check=True)

        print("Changes committed and pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
git_commit_and_push(message="Auto commit", branch="main")



def update():
    while True:
        # Read input from an external file or command-line argument
        try:
            with open("input.txt", "r") as file:
                input_code = file.read().strip()
        except FileNotFoundError:
            # input_code = input("Enter code (press Ctrl+D on a new line to finish):\n\n\n        ")
            input_code = ''
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
            # Commit and push changes before exiting
            git_commit_and_push("Auto commit before exit")
            break

update()
"""
Processed:         # Optionally, update an external file with the result
        with open("output.txt", "a") as file:
            file.write(output + "\n")

"""

"""
Processed: sjdn

"""

"""
Processed:         subprocess.run(["git", "commit", "-m", message], check=True)

"""

"""
Processed:         try:
            with open("input.txt", "r") as file:
                input_code = file.read().strip()

"""

"""
Processed: Processed:         # Optionally, update an external file with the result
        with open("output.txt", "a") as file:
            file.write(output + "\n")

"""
