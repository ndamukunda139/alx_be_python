def safe_divide(numerator, denominator):
    # performs division, handling potential errors: Division by Zero, Non-numeric Input
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:

        return "Error: Please enter numeric values only." 
