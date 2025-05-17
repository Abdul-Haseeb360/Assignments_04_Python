import random

def main():
    random_number = random.randint(1, 100)
    print("Welcome to the Guess My Number game!")
    print("Please think of a number between 1 and 100.")

    Get_number = int(input("Enter your guess: "))
    while Get_number != random_number:
        if Get_number < random_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        print()
        Get_number = int(input("Enter your guess: "))
    
    print("Congratulations!, you guessed the correct number:", random_number)

if __name__ == "__main__":
    main()