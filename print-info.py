 #!/usr/bin/env python3

"""Simple script that reads one line of input from the user and prints it."""

def main():
    try:
        user_input = input("Enter something: ")
    except EOFError:
        # Handle cases where input is piped or empty
        user_input = ""
    print("You entered:", user_input)


if __name__ == "__main__":
    main()
