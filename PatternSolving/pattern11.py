n = 4
"""for i in range(1, n+1):
    for j in range(1, i+1):
        if i%2!=0:
            print("*", end="")
        else:
            break

    print("")"""
for i in range(1, n+1):
    for j in range(1, i):
            print(" ", end="")   
    for j in range(1, (2*(n+1))-(2*i)):
            print("*", end="")
    

    print("")