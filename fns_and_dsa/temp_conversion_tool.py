FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


while True:
    try:
        value = float(input("Enter the temperature to convert: "))
        break
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")


temp = input(
    "Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()

if temp == "F":
    celsius = convert_to_celsius(value)
    print(f"{value}°F is {celsius}°C")
elif temp == "C":
    fahrenheit = convert_to_fahrenheit(value)
    print(f"{value}°C is {fahrenheit}°F")
else:
    print("Please enter a valid unit")
