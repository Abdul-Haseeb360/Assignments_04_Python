def main():
    user_year = int(input("Please Enter a year: "))

    
    if user_year % 4 == 0:  # Checking whether the provided year is evenly divisibly by 4
        if user_year % 100 == 0:  # Checking whether the provided year is evenly divisibly by 100
            if user_year % 400 == 0:  # Checking whether the provided year is evenly divisibly by 400
                print("That's a leap year!")
            else:  # (Not divisible by 400)
                print("That's not a leap year.")
        else:  # (Not divisible by 100)
            print("That's a leap year!")
    else:  # (Not divisible by 4)
        print("That's not a leap year.")

if __name__ == '__main__':
    main()