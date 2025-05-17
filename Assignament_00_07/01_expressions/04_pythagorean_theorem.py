import math

def  main():
    AB: float = float(input("Enter the length of side AB: "))
    AC: float = float(input("Enter the length of side AC: "))

    BC: float = math.sqrt(AB**2 + AC**2)
    print(f"The length of side BC (the hypotenuse) is: {str(BC)}") 

if __name__ == '__main__':
    main()