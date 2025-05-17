def main():
    user_name : str = input("\033[94m Enter your name: \033[0m")
    print(greet(user_name))

def greet(user_name):
    return "Greeting " +  user_name

if __name__ == '__main__':
    main()