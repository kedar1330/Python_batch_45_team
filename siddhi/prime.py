# Program to check whether a number is Prime or not

# Taking input from user
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a Prime Number")

else:
    
    prime = True

    # Checking divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            
            prime = False
            break

    # Displaying the result
    if prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is not a Prime Number")