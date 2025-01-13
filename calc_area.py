# Calculate Area of a Rectangle
# leng (float) = length
# wid (float) = width

def calc_area(leng, wid):
    return leng * wid

leng = float(input("Enter the rectangle length: "))
wid = float(input("Enter the rectangle width: "))

area = calc_area(leng, wid)
print (f"The area of the rectangle is: {area:.2f}.")