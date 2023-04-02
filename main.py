weight = float(input("Enter your weight: "))
unit = input("Is that in kilograms or in pounds? (K or L) ").lower()

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not valid")