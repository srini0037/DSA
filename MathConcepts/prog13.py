# To find if a number is Perfect or not
import math
num = input("Enter the number")
n = int(num)
sum = 1
for i in range(2,int(math.sqrt(n)+1)):
    if(n%i == 0):
        sum = sum + i
        if(n/i != i):
            sum = sum + (n//i)

if(sum == n):
    print(f"{n} is a Perfect number")
else:
    print(f"{n} is not a Perfect number")