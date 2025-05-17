INCHES_IN_FOOT: int = 12  

def main():

    user_feet = float(input("\033[1;3m Enter the number of feet: \033[0m")) 

    feet_to_inches = user_feet * INCHES_IN_FOOT
    print(f"{user_feet} feet = {feet_to_inches} inches")

if __name__ == '__main__':
    main()