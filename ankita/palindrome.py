# Take input from the user
num = int(input("Enter a number: "))

# Store the original number
original_num = num

# Variable to store the reversed number
reverse = 0

# Reverse the number
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Check whether it is a palindrome
if original_num == reverse:
    print(original_num, "is a Palindrome Number")
else:
    print(original_num, "is not a Palindrome Number")