# Python weight converter

weight  = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L):")

if unit == "K":
    weight = round((weight * 2.205),2)
    print(f"Weight in Pounds is: {weight} Lbs")
elif unit == "L":
    weight = round((weight / 2.205),2)
    print(f"Weight in Kilograms is: {weight} Kg")
else:
    print(f"{unit} is not valid")