"""
Chapter 1: Getting Started
AI concept: a single artificial neuron's "weighted sum" -- the basic
computation every neural network, no matter how deep, is built from.
Uses only what this chapter covers: variables, input(), print(), and
arithmetic.
"""
x1=float(input("Enter input 1 (e.g. hours studied): "))
x2=float(input("Enter input 2 (e.g. practice tests taken): "))
w1=0.6
w2=0.4
bias=-2.0
weighted_sum=x1 * w1 + x2 * w2 + bias
print("Weighted sum (the neuron's raw activation):", weighted_sum)
print("Turning this into a yes/no decision needs an if statement --")
print("that's exactly what Chapter 4 adds.")