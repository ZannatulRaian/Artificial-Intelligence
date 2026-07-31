"""
Chapter 8: More with Lists
"""
import random
dataset = [
    [1, 1, "A"],
    [6, 4, "B"],
    [9, 9, "B"],
    [4, 6, "A"],
    [2, 8, "A"],
]
candidates=[[5, 5], [7, 2], [3, 3]]
query_x, query_y=random.choice(candidates)
print("Query point:", query_x, query_y)
distances=[((query_x - row[0]) ** 2 + (query_y - row[1]) ** 2) ** 0.5 for row in dataset]
closest_distance=min(distances)
closest_row=dataset[distances.index(closest_distance)]

print("Distances to each training point:", [round(d, 3) for d in distances])
print("Predicted category:", closest_row[2])
print("Distance to nearest neighbor:", round(closest_distance, 3))
print()
print("Same 1-nearest-neighbor idea as Chapter 7, but the whole search")
print("loop now collapses into one list comprehension over the 2D list.")
print("We still only keep the single closest point -- Chapter 9's while")
print("loops will let us keep going until we've collected the k nearest")
print("neighbors, instead of just one.")
