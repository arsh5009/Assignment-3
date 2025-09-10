import math

# Ask the user for a number
try:
    number = float(input("Enter a number: "))

    # Square root
    sqrt_val = math.sqrt(number) if number >= 0 else "Not defined for negative numbers"

    # Natural logarithm (log base e)
    log_val = math.log(number) if number > 0 else "Not defined for zero or negative numbers"

    # Sine (input is in radians)
    sine_val = math.sin(number)

    # Display results
    print(f"\nResults for number {number}:")
    print(f"Square root: {sqrt_val}")
    print(f"Natural logarithm (base e): {log_val}")
    print(f"Sine (in radians): {sine_val}")

except ValueError:
    print("Please enter a valid numeric value.")