import os
import argparse
import subprocess

def generate_macros(names):
    passive_macro = "/w gm &{template:default} {{name=Passive Perception}}"
    active_macro = "/w gm &{template:default} {{name=Active Perception}}"
    for name in names:
        passive_macro += "{"
        active_macro += "{"
        passive_macro += f"{{{name}= [[10 + @{{{name}|perception_bonus}}]]}}"
        active_macro += f"{{{name}= [[1d20 + @{{{name}|perception_bonus}}]]}}"
        passive_macro += "}"
        active_macro += "}"
    ship_macro = "To add Quality Score, go to a ships token bars, instead of temp hp in the red bubble, assign it to the wisdom_mod attribute. \n In all rolls for the ship, have [[d20 + @{ wisdom_mod }]]. This makes the quality score changeable from the map token and used in everything."
    initiative_macro = "@{(target|wtype}&{template:simple} {{rname=^{init-u}}} {{mod=@{target|initiative_bonus}}} {{r1=[[@{target|initiative_style}+@{target|initiative_bonus}@{target|pbd_safe}[INIT] &{tracker}]]}} {{normal=1}} @{target|charname_output}"
    return passive_macro, active_macro, ship_macro

def main():
    parser = argparse.ArgumentParser(description="Generate group and individual macros for a list of player names.")
    parser.add_argument("player_names", type=str, help="Comma-separated list of player names. If you add spaces, IT WILL TOO.")
    parser.description = "Usage: python PartyMacroWriter.py 'Player1,Player2,Player3'"
    args = parser.parse_args()

    # Split the player names by comma
    player_names = [name.strip() for name in args.player_names.split(',')]

    # Generate macros
    passive_macro, active_macro, ship_macro, initiative = generate_macros(player_names)

    # Define the new file name
    new_file_name = "GroupMacros.txt"

    # Save the macros to the new file
    with open(new_file_name, 'w') as file:
        file.write("Passive Perception Macro:\n")
        file.write(passive_macro + "\n\n")
        file.write("Active Perception Macro:\n")
        file.write(active_macro + "\n\n")
        file.write("Ship Macro:\n")
        file.write(ship_macro + "\n\n")
        file.write("Initiative Macro:\n")
        file.write(initiative + "\n\n")

    # Call the script for each player name and append the result to the same file
    for name in player_names:
        result = subprocess.run(['python', 'PlayerMacroWriter.py', name, '--no-save'], capture_output=True, text=True)
        with open(new_file_name, 'a') as file:
            file.write(f"_______________________Macros for {name}:\n")
            file.write(result.stdout + "\n")
    print(f"Macros saved to {new_file_name}")

if __name__ == "__main__":
    main()