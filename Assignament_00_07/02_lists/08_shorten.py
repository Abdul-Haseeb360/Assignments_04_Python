MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()       # Removes last item
        print("Removed:", removed)

def get_lst():
    lst = []
    elem = input("Enter an item (or press enter to stop): ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter an item (or press enter to stop): ")
    return lst

def main():
    lst = get_lst()
    print("Original list:", lst)
    shorten(lst)
    print("Final list:", lst)

if __name__ == '__main__':
    main()
