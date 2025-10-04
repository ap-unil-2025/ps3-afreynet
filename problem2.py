"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
  
    F = (celsius * 9/5) + 32

    return F

print(celsius_to_fahrenheit(0))
def fahrenheit_to_celsius(fahrenheit):
    
    C = (fahrenheit - 32) * 5/9

    return C


def temperature_converter():
    value = float(input("Temperature value"))
    unit = str(input("C or F"))
    if unit == "C" :
        temp = celsius_to_fahrenheit(value)
        print(f"{temp:.2f} F")
    else:
        temp = fahrenheit_to_celsius(value)
        print(f"{temp:.2f} C")



# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()

    