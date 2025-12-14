import math

length = float(input("Enter the length of triangle : "))

height = float(input("Enter the height of triangle : "))

TriangleHypothesis =  math.sqrt(pow(length,2) + pow(height,2))

print(f"The Hypo of Triangle is {TriangleHypothesis}")