# Program to Reverse a number, which is wrong beacuse we arent storing the new integer and comparing
num = 5335
while(num > 0):
    digit = num%10
    num = num//10
    print(digit, end='')
print('')
if (num == digit):
    print("The Number is PALINDROME")
else:
    print("The Number is NOT A PALINDROME")