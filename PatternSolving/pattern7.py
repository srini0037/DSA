n=6

for i in range(1, n+1):
    for j in range((n-i)+2, 1, -1):
        print(j-1, end="")
    
    print()