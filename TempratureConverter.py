def convert_temperature(temp, scale):
    if scale.upper() == 'c':

        return (temp * 9/5) + 32
    elif scale.upper() == 'f':

        return (temp + 32) * 5/9
    
    else:
        return "Invalid scale! use 'c' for celsius or 'F' for fahrenheit."
    
celsius_temp = 25
fahrenheit_temp = 77

print(f"{celsius_temp}°C in Fahrenheit is: {convert_temperature(celsius_temp, 'C')}°F")
print(f"{fahrenheit_temp}°F in Celsius is: {convert_temperature(fahrenheit_temp, 'F')}°C")
