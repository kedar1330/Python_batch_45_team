# Take user input
num = int(input("Enter a number: "))

# Assume the number is prime
is_prime = True

# Numbers less than or equal to 1 are not prime
if num <= 1:
    is_prime = False
else:
    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

# Display the result
if is_prime:
    print(num, "is a Prime Number.")
else:
    print(num, "is Not a Prime Number.")