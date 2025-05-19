"""
I made my own version of the Perceptron algorithm using just python.

This is the formulaic version, meaning the data has to be perfect, with no errors, or else the algorithm will break.

It only works with 1 neighbor, with a 1D array.

GOAL: find B in the y = mx + b line equation. I'm just going to use M = 1 for this algorithm.

how you find B is you average the last -1 with the first 1 and that gives you the variable for the line.
"""
import matplotlib.pyplot as plt

X_train = [1,
           2,
           3,
           8,
           9,
           10] # features, descriptions, attributes, can be any number
y_train = [-1, -1, -1, 1, 1, 1,] # targets, labels, type, can be any character defining the numbers
X_test = 3.5 # int(input("input your data: ")) # the data that you want to see its nearest neighbors
y_test = -1 # the answer to see if your ML algorithm is right.

Xdist = [] 

# FINDING THE LINE

for i in range(len(X_train)):
    if y_train[i] == 1:
        # THE LAST -1
        LAST_NEGATIVE_ONE = X_train[i-1]
        # THE FIRST +1
        FIRST_POSITIVE_ONE = X_train[i]
        # FINDING THE LINE
        threshold = (LAST_NEGATIVE_ONE + FIRST_POSITIVE_ONE) / 2 # also known as "b"
        break

if X_test < threshold:
    print("X_test is to the left of the threshold (-1)")

elif X_test > threshold:
    print("X_test is to the right of the threshold (1)")

else:
    print("X_test is EXACTLY the threshold")

plt.scatter(X_train,[0] * len(X_train),c=y_train)
plt.scatter(X_test, 0, c="red", marker="x", s=60)
plt.scatter(threshold, 0, c=0)
plt.ylim([-3,10])
plt.xlim([0,11])
plt.colorbar()
plt.grid()
