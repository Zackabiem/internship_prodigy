# This function convert Celsius to Fahrenheit and Kelvin
def celsius_to_other(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# This Function  convert Fahrenheit to Celsius and Kelvin
def fahrenheit_to_other(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return celsius, kelvin

# This Function  convert Kelvin to Celsius and Fahrenheit
def kelvin_to_other(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return celsius, fahrenheit

# Main program
def temperature_conversion():
    try:
        # Prompt user for temperature value and unit
        temperature = float(input("Enter the temperature value: "))  # Ensure input is numeric
        unit = input("Enter the original unit (Celsius, Fahrenheit, Kelvin): ").strip().lower()
        
        # Validate the unit input
        if unit == "celsius":
            fahrenheit, kelvin = celsius_to_other(temperature)
            print(f"{temperature}° Celsius is equal to {fahrenheit}° Fahrenheit and {kelvin} Kelvin.")
        elif unit == "fahrenheit":
            celsius, kelvin = fahrenheit_to_other(temperature)
            print(f"{temperature}° Fahrenheit is equal to {celsius}° Celsius and {kelvin} Kelvin.")
        elif unit == "kelvin":
            celsius, fahrenheit = kelvin_to_other(temperature)
            print(f"{temperature} Kelvin is equal to {celsius}° Celsius and {fahrenheit}° Fahrenheit.")
        else:
            print("Invalid unit. Please enter either Celsius, Fahrenheit, or Kelvin.")
    
    except ValueError:
        print("Please enter a valid numeric value for temperature.")

# Execute the program
temperature_conversion()
