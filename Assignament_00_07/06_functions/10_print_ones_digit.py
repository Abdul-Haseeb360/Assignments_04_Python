def print_ones_digit(user_num):
    one_digit = user_num % 10
    print("The ones digit is", one_digit)


def main():
    user_num = int(input("\033[94m Enter a number: \033[0m"))
    print_ones_digit(user_num)


if __name__ == "__main__":
    main()
43