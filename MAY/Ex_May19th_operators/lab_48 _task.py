# Input: lengths of the three sides
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

# Check if the sides can form a triangle (Triangle Inequality Theorem)
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The entered sides do not form a valid triangle.")
