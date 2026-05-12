# Program to Reverse a number
num = 5335
sum = 0
while(num > 0):
    digit = num%10
    sum = (10*sum) + digit
    num = num // 10

print(sum)
num = 5335
if (num == sum):
    print("The Number is PALINDROME")
else:
    print("The Number is NOT A PALINDROME")