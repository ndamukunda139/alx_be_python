# Declare variables 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit): 
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) +32
    return fahrenheit

def main():
    temperature = float(input("Enter the temperature to convert:")) 
    temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
    if temperature_unit.upper() == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print (f"{temperature}°C is {converted_temp}°F")
    elif temperature_unit.upper() == 'F':
        converted_temp = convert_to_celsius(temperature)
        print (f"{temperature}°F is {converted_temp}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")
    

if __name__ == "__main__":
    main()

