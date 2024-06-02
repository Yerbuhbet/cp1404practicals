def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = convert_c_to_f(celsius)
    print(f"{celsius} C is {fahrenheit} F")
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = convert_f_to_c(fahrenheit)
    print(f"{fahrenheit} F is {celsius} C")