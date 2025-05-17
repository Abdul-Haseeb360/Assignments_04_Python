def main():
    print(in_range(5, 1, 10))
def in_range(n, low, high):

    if n >= low and n <= high:
        return True
    return False    

if __name__ == '__main__':
    main()