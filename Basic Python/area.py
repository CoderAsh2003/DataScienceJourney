def calculate_area(base,height,shape):
    if shape == "triangle":
        area = 1/2*base*height
    if shape == "rectangle":
        area = base*height
    return area
