def get_last_element(lst):
    print(lst[-1]) 


def get_lst():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst


def main():
    lst = get_lst()
    get_last_element(lst)


if __name__ == '__main__':
    main()
