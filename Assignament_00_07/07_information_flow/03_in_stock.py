def main():
    fruits: str = input("Enter a fruit: ")
    stock = num_in_stock(fruits)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)


def num_in_stock(fruits):

    if fruits == "apple":
        return 2
    if fruits == "banana":
        return 4
    if fruits == "mango":
        return 8
    else:
        return 0


if __name__ == '__main__':
    main()
