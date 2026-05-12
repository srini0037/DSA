#Given an integer n, find all the prime numbers upto n

num = 17

for i in range (2, num+1):
    count = 0
    for j in range(2, num+1):
        if i%j == 0:
            count = count+1
    if count == 1:
        print(i)



    