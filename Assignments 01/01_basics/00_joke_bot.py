PROMPT = "What do you want?"
JOKE = "Here is a joke for you! Why do programmers prefer dark mode? Because the light attracts bugs. 🐞😂"
SORRY = "Sorry I only tell jokes"

def main():
    user_input = input(PROMPT + ("\033[94m  \033[0m"))
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
