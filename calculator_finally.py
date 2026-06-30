

def main():

    print()
    print("          Welcome on my project!!!")


    while True:

        print()
        print("1.+")
        print("2.-")
        print("3.*")
        print("4./")
        print("5.//")
        print("6.%")
        print("7.Quit")

        try:
            user_choice = float(input("Enter action 1-7: ".strip()))
        except ValueError:
            print("Please enter a number 1-7..")
            continue

        if user_choice == 7:
            print("Goodbye!")
            break

        try:
            a = float(input("Enter first number: ".strip()))
            b = float(input("Enter second number: ".strip()))
            print()
        except ValueError:
            print("Please enter a number..")
            continue

        if user_choice == 1:
            print(a + b)

        elif user_choice == 2:
            print(a - b)
        elif user_choice == 3:
            print(a * b)

        elif user_choice in [4, 5, 6]:
            if a == 0 or b == 0:
                print("U can not divide by 0!")
            else:
                if user_choice == 4:
                    print(a / b)
                elif user_choice == 5:
                    print(a // b)
                elif user_choice == 6:
                    print(a % b)

        else:
            print("Invalid code!Try again..")

if __name__ == "__main__":
    main()

