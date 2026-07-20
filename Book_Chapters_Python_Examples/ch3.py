"""
Chapter 3: Numbers
AI concept: Euclidean distance -- the "how far apart are these two
things" measurement that powers k-Nearest Neighbors, k-means
clustering, and plenty of other AI algorithms. It's built entirely
from the math operators and order of operations this chapter covers.
"""
import random
x1=3
y1=4
x2=random.randint(0, 10)
y2=random.randint(0, 10)
print("Point A:", x1, y1)
print("Point B:", x2, y2)

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print()
print("Euclidean distance between A and B:", round(distance, 3))
print("This exact formula is what k-Nearest Neighbors uses to decide")
print("which training points are 'closest' to a new one.")