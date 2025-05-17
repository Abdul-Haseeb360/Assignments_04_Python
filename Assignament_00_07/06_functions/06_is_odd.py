def main():
    for i in range(10):
        if odd_num(i):
            print("This is odd")
        else:
            print("This is even")

def odd_num(value: int):
    reminder = value % 2
    return reminder == 1

if __name__ == "__main__":
    main()