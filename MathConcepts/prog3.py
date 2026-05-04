n = 7879
count = 0
fnum = 0
lnum = n%10
while(n>0):
    digit = n%10
    fnum = digit
    n = n//10
sum = fnum + lnum
print(sum)