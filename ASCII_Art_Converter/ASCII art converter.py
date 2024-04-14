import pyfiglet
from termcolor import colored
import subprocess

# Function to convert text to ASCII art
def text_to_ascii_art(text, font="standard", color="white"):
    try:
        if font == "standard":
            ascii_art = pyfiglet.figlet_format(text)
        elif font == "block":
            ascii_art = pyfiglet.figlet_format(text, font="block")
        elif font == "doh":
            ascii_art = pyfiglet.figlet_format(text, font="doh")
        elif font == "bubble":
            ascii_art = pyfiglet.figlet_format(text, font="bubble")
        else:
            return "Invalid font. Choose 'standard', 'block', 'doh', or 'bubble'."

        return colored(ascii_art, color)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    subprocess.run(["figlet", "ASCII Art Converter"])
    print("Welcome to the Text to ASCII Art Converter!")

    while True:
        print("\nMenu:")
        print("1. Convert Text to Standard ASCII Art")
        print("2. Convert Text to Block ASCII Art")
        print("3. Convert Text to Doh ASCII Art")
        print("4. Convert Text to Bubble ASCII Art")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == '1':
            text = input("Enter the text to convert: ")
            result = text_to_ascii_art(text, "standard")
            print(result)
        elif choice == '2':
            text = input("Enter the text to convert: ")
            result = text_to_ascii_art(text, "block")
            print(result)
        elif choice == '3':
            text = input("Enter the text to convert: ")
            result = text_to_ascii_art(text, "doh")
            print(result)
        elif choice == '4':
            text = input("Enter the text to convert: ")
            result = text_to_ascii_art(text, "bubble")
            print(result)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")
