a = 125
b = 3
k = 4
count = 0
prod = 1
for i in range(1, b+1):
    prod = prod*a
print(prod)
while(prod>0):
    digit = prod%10
    count = count+1
    prod = prod//10
    if count == k:
        break

print(digit)