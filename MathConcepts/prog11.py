#Given an integer n, find all the divisors of n

num = 17
count = 0
for i in range (1, num+1):
    if num%i == 0:
        print(i)



    