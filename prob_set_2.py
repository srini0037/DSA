#Write a program to check whether a triangle can be formed with the given values for the angles.
a1 = int(input("Enter the first angle: "))
a2 = int(input("Enter the second angle: "))
a3 = int(input("Enter the third angle: "))
if a1 + a2 + a3 == 180:
    print("The triangle can be formed.")
else:
    print("The triangle cannot be formed.")