C =  299792458 

def main():

    user_mass = float(input("\033[1;3m Enter the mass in kilograms: \033[0m"))
    energy = user_mass * (C ** 2)

    print("e = m * C^2...")
    print("m = " + str(user_mass) + " kg")
    print("C = " + str(C) + " m/s")
    print(f"Energy: {energy} Joules")
if __name__ == '__main__':
    main()