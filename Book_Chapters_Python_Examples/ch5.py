"""
Chapter 5: Miscellaneous Topics I
AI concept: nearest-neighbor search, done completely by hand using the
"track the smallest value seen so far" pattern this chapter teaches for
finding a min/max. This is the core step behind the k-Nearest Neighbors
algorithm -- before Chapter 7's lists make it easy.
"""
query_x=5
query_y=5

p1_x,p1_y=1,1
p2_x,p2_y=6,4
p3_x,p3_y=9,9
p4_x,p4_y=4,6
p5_x,p5_y=2,8

closest_distance=((query_x-p1_x)**2+(query_y-p1_y)**2)**0.5
closest_label="p1"

distance=((query_x-p2_x)**2+(query_y-p2_y)**2)**0.5
if distance<closest_distance:
    closest_distance=distance
    closest_label="p2"

distance=((query_x-p3_x)**2+(query_y-p3_y)**2)**0.5
if distance<closest_distance:
    closest_distance=distance
    closest_label="p3"

distance=((query_x-p4_x)**2+(query_y-p4_y)**2)**0.5
if distance<closest_distance:
    closest_distance=distance
    closest_label="p4"

distance=((query_x-p5_x)**2+(query_y-p5_y)**2)**0.5
if distance<closest_distance:
    closest_distance=distance
    closest_label="p5"

print("Nearest neighbor to (5, 5) is:",closest_label)
print("Distance:",round(closest_distance,3))

print()
print("Doing this by hand for 5 points is already tedious --")
print("Chapters 7-9 (lists and loops) will make it automatic.")