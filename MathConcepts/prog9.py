#Given an integer n, find the number of divisors of n that are divisible by 3.

num = 6

for i in range(1, num+1):
    if(num%i == 0):
        if(i%3 == 0):
            print(i)
    