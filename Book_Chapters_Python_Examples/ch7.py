"""
Chapter 7: Lists
AI concept: a real k-Nearest Neighbors classifier (k=1). This is
Chapter 5's by-hand nearest-neighbor search, but now a list and a for
loop do the repetitive work automatically instead of five almost-
identical if blocks.
"""
train_x=[1,6,9,4,2]
train_y=[1,4,9,6,8]
train_label=["A","B","B","A","A"]

query_x=5
query_y=5

closest_distance=((query_x-train_x[0])**2+(query_y-train_y[0])**2)**0.5
closest_label=train_label[0]

for i in range(1,len(train_x)):
    distance=((query_x-train_x[i])**2+(query_y-train_y[i])**2)**0.5
    if distance<closest_distance:
        closest_distance=distance
        closest_label=train_label[i]

print("Query point:",query_x,query_y)
print("Predicted category:",closest_label)
print("Distance to nearest neighbor:",round(closest_distance,3))