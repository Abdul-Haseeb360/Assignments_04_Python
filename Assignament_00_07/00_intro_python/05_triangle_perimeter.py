def main():
    side1 = input("Enter the length of the first side of the triangle: ")
    side2 = input("Enter the length of the second side of the triangle: ")
    side3 = input("Enter the length of the third side of the triangle: ")

    side1 = float(side1)
    side2 = float(side2)
    side3 = float(side3)

    print(f"The perimeter of the triangle is: {side1 + side2 + side3}")
if __name__ == '__main__':
    main()