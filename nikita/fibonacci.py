# Fibonacci series program
# Accept the number of terms from the user
n=int(input("Enter the number of terms:"))
# Handle invalid input
if n<=0:
    print("Please enter a positive integer.")
else:
    a=0
    b=1
    print("Fibonacci Series:")
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b