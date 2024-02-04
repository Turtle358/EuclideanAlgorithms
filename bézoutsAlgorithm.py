# Function to calculate the greatest common divisor (GCD) using the Euclidean algorithm
def euclideanGCD(a: int, b: int) -> tuple[list, list, int]:
    # Lists to store the quotients and remainders at each step of the algorithm
    quotients = []
    remainders = []

    # Iterate until b becomes 0, applying the Euclidean algorithm
    while b != 0:
        quotient = a // b  # Calculate the quotient
        remainder = a % b  # Calculate the remainder
        quotients.append(quotient)  # Store the quotient
        remainders.append(remainder)  # Store the remainder
        a, b = b, remainder  # Update a and b for the next iteration

    # Return the lists of quotients and remainders, and the final GCD
    return quotients, remainders, a


# Function to apply Bézout's algorithm and find the coefficients x, y, and GCD
def bezoutsAlgorithm(a: int, b: int) -> tuple[int, int, int]:
    # Obtain the lists of quotients, remainders, and the GCD using Euclidean algorithm
    quotients, remainders, gcd = euclideanGCD(a, b)

    # Initialize coefficients for Bezout's identity
    x = 0
    y = 1

    # Iterate backward through the list of quotients to find coefficients
    for i in range(len(quotients) - 2, -1, -1):  # Go backwards (up the list), start at 2nd to back item, since that is what you do with bézout's identity
        x, y = y, x - y * quotients[i]  # Update coefficients

    # Return the coefficients x, y, and the GCD
    return x, y, gcd


# Get input from the user for two numbers
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

# Call the Bezout's algorithm function with the input numbers
x, y, gcd = bezoutsAlgorithm(num1, num2)

print(f'\n{gcd} = {num1}({x}) + {num2}({y})')
