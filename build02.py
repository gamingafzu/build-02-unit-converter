def kilometer_to_miles(kilometers):
    return kilometers * 0.621371


def miles_to_kilometer(miles):
    return miles / 0.621371


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


while True:

    print("1. kilometer to miles")
    print("2. miles to kilometer")
    print("3. celsius to fahrenheit")
    print("4. fahrenheit to celsius")
    print("5. exit")

    choice = input("Choose an option: ")

    try:

        if choice == "1":
            km = float(input("Enter distance in kilometers: "))
            if km < 0:
                print("Distance cannot be negative. Please enter a valid distance.")
                continue
            miles = kilometer_to_miles(km)
            print(f"{km} kilometers is equal to {miles} miles.")

        elif choice == "2":
            miles = float(input("Enter distance in miles: "))
            if miles < 0:
                print("Distance cannot be negative. Please enter a valid distance.")
                continue
            km = miles_to_kilometer(miles)
            print(f"{miles} miles is equal to {km} kilometers.")

        elif choice == "3":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(
                f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit."
            )

        elif choice == "4":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(
                f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius."
            )

        elif choice == "5":
            print("goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1 to 5.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
