num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Handle division by zero
if num2 != 0:
    quotient_result = num1 / num2
else:
    quotient_result = "Undefined (division by zero)"

print(f"Results of your two numbers:")
print(f"Addition: {sum_result}")
print(f"Subtraction: {difference_result}")
print(f"Multiplication: {product_result}")
print(f"Division: {quotient_result}")