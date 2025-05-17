def double(user_input):
    return user_input * 2

def main():
    user_input = int(input("\033[94m Enter a number: \033[0m"))
    number_double = double(user_input)
    print(f"The double of {user_input} is {number_double}")



if __name__ == "__main__":
    main()
