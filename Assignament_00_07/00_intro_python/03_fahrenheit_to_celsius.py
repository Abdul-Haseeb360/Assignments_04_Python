def main():
    user_temp_fahrenheit = float(input("\033[1;3m Enter the temperature in Fahrenheit \033[0m"))
    fahrenheit_to_Celsius = (user_temp_fahrenheit - 32) * 5.0/9.0

    print(f"Temprature: {user_temp_fahrenheit}F = {fahrenheit_to_Celsius}C")

if __name__ == '__main__':
    main()