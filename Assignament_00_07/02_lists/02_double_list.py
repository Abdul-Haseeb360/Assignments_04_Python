def main():
    double_numbers: list[int] = [1, 2, 3, 4] 

    for i in range(len(double_numbers)):  
        elem_at_index = double_numbers[i]  
        double_numbers[i] = elem_at_index * 2  

    print(double_numbers) 

if __name__ == '__main__':
    main()