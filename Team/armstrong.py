#Accept input from the user

num=int(input("Enter the Number:"))

#store original number for comparison 

original_num=num
num_digit=len(str(num))
sum_of_powers=0

#Count total digits
#Calculate the armstrong sum
temp=num
while temp>0:
    digit=temp%10
    sum_of_powers+=digit**num_digit
    temp//=10

#Compare with the original number
#display the result.

if sum_of_powers==original_num:
    print(f"{original_num} is an armstrong number")
else:
    print(f"{original_num} is not an armstrong number")
