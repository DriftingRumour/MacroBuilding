import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Generate macros for a player.")
    parser.add_argument("player_name", type=str, help="Player name to generate macros for.")
    parser.add_argument("--no-save", action="store_true", help="Do not save to file, return macros instead.")
    args = parser.parse_args()

    # Define the path to the Macros.txt file
    macros_file = 'Macros.txt'

    # Check if Macros.txt exists
    if not os.path.exists(macros_file):
        print(f"Error: {macros_file} does not exist.")
        return

    # Read the content of Macros.txt
    with open(macros_file, 'r') as file:
        content = file.read()

    # Replace all instances of PLAYER_NAME with the provided name
    modified_content = content.replace("PLAYER_NAME", args.player_name)

    # Define the new file name
    if args.no_save:
        print(modified_content)
        return modified_content
    else:
        new_file_name = f"{args.player_name}_Macros.txt"
        # Save the modified content to the new file
        with open(new_file_name, 'w') as file:
            file.write(modified_content)
        print(f"Modified content saved to {new_file_name}")

if __name__ == "__main__":
    main()