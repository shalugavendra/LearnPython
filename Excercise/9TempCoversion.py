#!/usr/bin/env python3

unit = input("Is this tempature in Celsius or Fahrenheit? (C, F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9/5) + 32, 2)
    print(f"Temperature in Fahrenheit is: {temp} °F")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 2)
    print(f"Temperature in Celsius is: {temp} °C")
else:
    print(f"{unit} is an invalid unit of measurement")


"""
Simple temperature conversion CLI.
Supports Celsius, Fahrenheit and Kelvin.
"""
'''
def c_to_f(c): return c * 9/5 + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15
def f_to_k(f): return c_to_k(f_to_c(f))
def k_to_f(k): return c_to_f(k_to_c(k))

def prompt_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")

def main():
    menu = (
        "1) Celsius -> Fahrenheit\n"
        "2) Fahrenheit -> Celsius\n"
        "3) Celsius -> Kelvin\n"
        "4) Kelvin -> Celsius\n"
        "5) Fahrenheit -> Kelvin\n"
        "6) Kelvin -> Fahrenheit\n"
        "7) Exit\n"
    )
    while True:
        print(menu)
        choice = input("Choose an option (1-7): ").strip()
        if choice == "7":
            break
        if choice not in {"1","2","3","4","5","6"}:
            print("Invalid choice.\n")
            continue

        value = prompt_float("Enter temperature: ")
        if choice == "1":
            out = c_to_f(value); unit = "°F"
        elif choice == "2":
            out = f_to_c(value); unit = "°C"
        elif choice == "3":
            out = c_to_k(value); unit = "K"
        elif choice == "4":
            out = k_to_c(value); unit = "°C"
        elif choice == "5":
            out = f_to_k(value); unit = "K"
        elif choice == "6":
            out = k_to_f(value); unit = "°F"

        print(f"Result: {out:.2f} {unit}\n")

if __name__ == "__main__":
    main()
    '''

