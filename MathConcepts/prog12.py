import math

num = 20736
count = 0
for i in range(2,int(math.sqrt(num))+1):
    if num%i == 0:
        count = count +1
if count == 1:
    print("it is prime")
else:
    print("it is not")