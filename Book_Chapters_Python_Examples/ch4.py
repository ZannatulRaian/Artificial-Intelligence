"""
Chapter 4: If statements
AI concept: finishing the artificial neuron from Chapter 1. A neuron's
weighted sum becomes a real decision once we add a threshold check --
exactly what if statements give us. This is a full single-layer
perceptron: weighted sum + activation.
"""
x1=float(input("Enter input 1 (e.g. hours studied): "))
x2=float(input("Enter input 2 (e.g. practice tests taken): "))

w1=0.6
w2=0.4
bias=-2.0

weighted_sum = x1 * w1 + x2 * w2 + bias
print("Weighted sum:", round(weighted_sum, 3))

if weighted_sum > 0:
    print("Prediction: PASS")
elif weighted_sum == 0:
    print("Prediction: Borderline (exactly on the decision boundary)")
else:
    print("Prediction: FAIL")