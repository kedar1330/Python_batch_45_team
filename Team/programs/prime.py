# Program to check whether a number is Prime or not


# Taking input from user
num = int(input("Enter a number: "))

# Prime number checking logic
if num <=1:
    print ("num is not a prime")

else:

    prime=True

    for i in  range(2,num):
        if num % i==0:
            prime==False
            break
    # Display result
    if prime:
        print(num, "is a Prime Number")
    else:
        print(num, "is not a Prime Number")
