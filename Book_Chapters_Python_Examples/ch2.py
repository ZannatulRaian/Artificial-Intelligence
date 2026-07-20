"""
Chapter 2: For loops
AI concept: gradient descent -- the algorithm that trains almost every
machine learning model, including neural networks. A for loop repeatedly
nudges one number (a "weight") a little closer to the value that makes
our tiny model's prediction correct.
"""
x=4
target=20
w=0.5
learning_rate=0.01
for step in range(60):
  prediction=w*x
  error=prediction-target
  gradient=2*x*error
  w=w-learning_rate*gradient
  print("step", step, "w = ", round(w,4), "prediction = ", round(prediction, 4))

print()
print("Final weight: ", round(w, 4))
print("Target was for w*x to equal", target , "- see how close the prediction got.")
