# Take user input
num = int(input("Enter a number: "))

# Initialize the first two Fibonacci numbers
first = 0
second = 1

# Assume the number is not in the series
found = False

# Check if the number is 0
if num == 0:
    found = True

# Generate Fibonacci numbers until they reach or exceed the input number
while first <= num:
    if first == num:
        found = True
        break

    # Calculate the next Fibonacci number
    next_num = first + second

    # Update the values
    first = second
    second = next_num

# Display the result
if found:
    print(num, "is a Fibonacci Number.")
else:
    print(num, "is Not a Fibonacci Number.")