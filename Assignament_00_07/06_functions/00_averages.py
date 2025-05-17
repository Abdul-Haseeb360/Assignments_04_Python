def average(a:float, b:float):
    sum  = a + b
    return sum / 2

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"The average of {a} and {b} is {average(a, b)}")

if __name__ == "__main__":
    main()