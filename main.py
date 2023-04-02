# Get the user's weight as a float
weight = float(input("Enter your weight: "))

# Get the unit of measurement for the weight (Kilograms or Pounds)
unit = input("Is that in kilograms or in pounds? (K or L) ").lower()

# Check if the unit is Kilograms
if unit == "k":
    # Convert the weight from Kilograms to Pounds
    weight = weight * 2.205
    # Set the unit to Pounds
    unit = "Lbs."
    # Print the converted weight in Pounds
    print(f"Your weight is: {round(weight, 2)} {unit}")
# Check if the unit is Pounds
elif unit == "l":
    # Convert the weight from Pounds to Kilograms
    weight = weight / 2.205
    # Set the unit to Kilograms
    unit = "Kgs."
    # Print the converted weight in Kilograms
    print(f"Your weight is: {round(weight, 2)} {unit}")
# If the unit is neither Kilograms nor Pounds
else:
    # Print an error message
    print(f"{unit} is not valid")