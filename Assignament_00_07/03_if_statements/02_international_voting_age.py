PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():

    user_age = int(input("\033[94m How old are you? \033[0m"))

    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is" + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is" + str(PETURKSBOUIPO_AGE) + ".")

    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau  where the voting age is" + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Stanlau  where the voting age is" + str(PETURKSBOUIPO_AGE) + ".")
    
    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua  where the voting age is" + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Mayengua  where the voting age is" + str(PETURKSBOUIPO_AGE) + ".")
    
if __name__ == '__main__':
    main()