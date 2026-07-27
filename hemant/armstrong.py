# Take input from the user
num = int(input("Enter a number: "))

# Store the original number
original_num = num

# Find the number of digits
digits = len(str(num))

# Variable to store the sum of powered digits
sum = 0

# Calculate the sum of each digit raised to the power of total digits
while num > 0:
    digit = num % 10      
    sum = sum + (digit ** digits)   
    num = num // 10          

# Check whether the number is an Armstrong number
if sum == original_num:
    print(original_num, "is an Armstrong Number")
else:
    print(original_num, "is not an Armstrong Number")