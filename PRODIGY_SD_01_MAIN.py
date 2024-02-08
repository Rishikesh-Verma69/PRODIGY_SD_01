def kelvin_to_celsius(value):
    return value - 273.15

def celsius_to_kelvin(value):
    return value + 273.15

def kelvin_to_fahrenheit(value):
    kelvin_to_celsius(value)
    return celcius_to_fahrenheit(value)

def fahrenheit_to_kelvin(value):
    fahrenheit_to_celsius(value)
    return celsius_to_kelvin(value)

def fahrenheit_to_celsius(value):
    value = (value - 32) * 5 / 9
    return value

def celcius_to_fahrenheit(value):
    value = 32 + (value*9)/5
    return value


def main():
    go = 1
    while go==1:
        print("Please select the Input Unit:\n 1. Celsius\n 2. Fahrenheit\n 3. Kelvin\n Only enter the numberings.\n")
        unit1 = int(input(""))
        print("\n")
        if unit1<0 or unit1>3:
            print("Invalid. !!!!!!!!")

        else:
            value = int(input("Please enter the Value: \n"))
            print("Select the unit you would like to calculate: \n 1. Celsius\n 2. Fahrenheit \n 3. Kelvin\n")
            unit2 = int(input(""))
            print("\n")

            if unit1 == unit2:
                print("your Value is equal to : ")
                print(value)

            if unit1 == 1 and unit2 == 2:
                print("your Value is equal to : ")
                print(celcius_to_fahrenheit(value))

            if unit1 == 1 and unit2 == 3:
                print("your Value is equal to : ")
                print(celsius_to_kelvin(value))

            if unit1 == 2 and unit2 == 1:
                print("your Value is equal to : ")
                print(fahrenheit_to_celsius(value))

            if unit1 == 3 and unit2 == 1:
                print("your Value is equal to : ")
                print(kelvin_to_celsius(value))

            if unit1 == 2 and unit2 == 3:
                print("your Value is equal to : ")
                print(fahrenheit_to_kelvin(value))

            if unit1 == 3 and unit2 == 2:
                print("your Value is equal to : ")
                print(kelvin_to_fahrenheit(value))

        print("\n")
        print("If you want to run this program again, enter 1 else enter 0: \n")
        go = int(input(""))



main()
