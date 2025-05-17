AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    while True:
        user_input = input("\033[94m Please type the following affirmation: \033[0m" + AFFIRMATION + "\n")
    
        if user_input == AFFIRMATION:
            print("That's right! :)")
        else:
            print("Hmmm That was not the affirmation.!")
        
if __name__ == '__main__':
    main()