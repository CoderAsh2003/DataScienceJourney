# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width

# If no shape is supplied then it should take triangle as a default shape

# Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print

# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def calculate_area(base,height,shape):
    if shape == "triangle":
        area = 1/2*base*height
    if shape == "rectangle":
        area = base*height
    return area

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
shape = input("Enter shape(triangle or rectangle): ")
print(f"Area of triangle is: {calculate_area(base,height,shape)}")

def print_pattern(n):
    for i in range(n):
        s = ''
        for j in range(i+1):
            s += '*'
        print(s) 
print_pattern(5)
