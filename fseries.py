#take input from user
n=int(input("Enter the number of terms:"))
a,b=0,1
print (f"Fibonacci Series of {n} numbers:")
#for loop to iterate through the range
for i in range(n):
    print(a,end=" ")
    a=b,a+b