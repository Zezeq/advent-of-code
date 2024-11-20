

def greet(name):
    """Function to greet a user by their name."""
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"

def main():
    """Main function to execute greet()"""
    name = input("Enter your name: ")
    print(greet(name))

if __name__ == "__main__":
    print("Welcome to advent of Code 2024!")
    main()