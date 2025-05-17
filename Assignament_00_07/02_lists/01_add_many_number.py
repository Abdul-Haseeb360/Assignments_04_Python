def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers: list[int] = [5, 10, 15, 20]  
    sum_of_numbers: int = sum_numbers(numbers)  
    print(sum_of_numbers)  
    
if __name__ == '__main__':
    main()