def divisors_num(num:int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    user_divisor = int(input("Enter a number: "))
    divisors_num(user_divisor)

if __name__ == '__main__':
    main()