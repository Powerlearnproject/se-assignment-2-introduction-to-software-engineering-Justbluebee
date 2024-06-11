"""D
Part (A): """

import numpy as np

vector = np.arange(1, 11) + 1
print(vector)

#%%
"""Part (B):"""

i = np.arange(1, 11).reshape((10, 1))
j = np.arange(1, 11).reshape((1, 10))
A = i + j
print(A)

#%%
"""Part (C): Create a "data set" with 50 examples, each with five dimensions:"""

import numpy.random as npr

data = np.exp(npr.randn(50, 5))
print(data)

#%%
"""Part (D): Compute the mean and standard deviation of each column:"""

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
print("Mean:", mean)
print("Standard Deviation:", std)

#%%
"""Part (E): Standardize the data matrix:"""

normalized = (data - mean) / std
print(normalized)

#%%
"""Verification: Compute the mean and standard deviation of the columns of normalized:"""

normalized_mean = np.mean(normalized, axis=0)
normalized_std = np.std(normalized, axis=0)
print("Normalized Mean:", normalized_mean)
print("Normalized Standard Deviation:", normalized_std)

#%%
"""E
Part (A): Create a variable named foo that stores an array of numbers from 0 to 29, inclusive. Print foo and its shape:"""

foo = np.arange(30)
print("foo:", foo)
print("Shape of foo:", foo.shape)

#%%
"""Part (B): Use the reshape function to change foo to a validly-shaped two-dimensional matrix and store it in a new variable called bar. Print bar and its shape:"""
bar = foo.reshape(5, 6)
print("bar:\n", bar)
print("Shape of bar:", bar.shape)

#%%
"""Part (C): Create a third variable, baz, that reshapes foo into a valid three-dimensional shape. Print baz and its shape:"""

baz = foo.reshape(2, 3, 5)
print("baz:\n", baz)
print("Shape of baz:", baz.shape)

#%%
"""Part (D): Use two-dimensional array indexing to set the first value in the second row of bar to -1. Now look at foo and baz. Did they change? Explain what’s going on:"""

bar[1, 0] = -1
print("Updated bar:\n", bar)
print("foo:", foo)
print("baz:\n", baz)

#%%
"""Part (E): Use the sum function on baz:

Sum baz over its second dimension and print the result:"""

sum_over_second = np.sum(baz, axis=1)
print("Sum over second dimension:\n", sum_over_second)

#%%
"""Sum baz over its third dimension and print the result:"""

sum_over_third = np.sum(baz, axis=2)
print("Sum over third dimension:\n", sum_over_third)

#%%
"""Sum baz over both its first and third dimensions and print the result:"""

sum_over_first_and_third = np.sum(baz, axis=(0, 2))
print("Sum over first and third dimensions:\n", sum_over_first_and_third)

#%%
"""Part (F): Perform slicing operations on bar:
Slice out the second row of bar and print it:"""

second_row = bar[1, :]
print("Second row of bar:", second_row)

#%%
"""Slice out the last column of bar using the -1 notation and print it:"""

last_column = bar[:, -1]
print("Last column of bar:", last_column)

#%%
"""Slice out the top right 
2
×
2
2×2 submatrix of bar and print it:"""

top_right_2x2 = bar[:2, -2:]
print("Top right 2x2 submatrix of bar:\n", top_right_2x2)

#%%
"""A. Write a python program to out put the following shapes
"""

import matplotlib.pyplot as plt

# Data to plot
labels = ['Kisumu', 'Mombasa', 'NAKURU']
sizes = [35, 35, 30]
colors = ['blue', 'orange', 'green']
explode = (0.1, 0, 0)  # explode 1st slice (Kisumu)

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#%%
import matplotlib.pyplot as plt

# Data to plot
labels = ['FORD', 'BMW', 'AUDI', 'MERCEDES', 'JAGUAR', 'TESLA']
sizes = [20, 15, 15, 15, 10, 25]
colors = ['green', 'orange', 'blue', 'brown', 'purple', 'red']
explode = (0, 0, 0, 0, 0, 0.1)  # explode the TESLA slice
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#%%
import matplotlib.pyplot as plt

# Data to plot
categories = ['SSET', 'Education', 'Health sci', 'Business', 'Law']
values = [20, 15, 35, 10, 25]

# Create bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')

# Show the plot
plt.show()

#%%
import numpy as np
import matplotlib.pyplot as plt

# Define the heart shape function
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Plot the heart shape
plt.figure(figsize=(6, 6))
plt.plot(x, y)

# Plot the center point
plt.plot(0, 0, 'ro')

# Set aspect ratio and limits
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-20, 20)
plt.ylim(-20, 15)

# Display the plot
plt.show()

#%%
"""B. Write python programs to 
How to Remove rows in Numpy array that contains non-numeric values?"""

import numpy as np

# Sample numpy array with non-numeric values
arr = np.array([
    [1, 2, 3],
    [4, 5, 'a'],
    [7, 8, 9]
])

# Function to remove rows with non-numeric values
def remove_non_numeric_rows(arr):
    return np.array([row for row in arr if np.all(np.char.isnumeric(row.astype(str)))])

cleaned_array = remove_non_numeric_rows(arr)
print(cleaned_array)

#%%
"""Check whether a Numpy array contains a specified row"""

import numpy as np

# Sample numpy array
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Specified row to check
specified_row = np.array([4, 5, 6])

# Function to check if specified row is in array
def contains_row(arr, row):
    return any(np.array_equal(r, row) for r in arr)

contains = contains_row(arr, specified_row)
print(contains)

#%%
"""Remove single-dimensional entries from the shape of an array"""

import numpy as np

# Sample numpy array with single-dimensional entries
arr = np.array([[[1, 2, 3]]])

# Remove single-dimensional entries
squeezed_array = np.squeeze(arr)
print(squeezed_array)
print(squeezed_array.shape)

#%%
"""Find the number of occurrences of a sequence in a NumPy array"""

import numpy as np

# Sample numpy array
arr = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5])

# Sequence to find
sequence = np.array([1, 2, 3])

# Function to find occurrences of a sequence
def count_sequence_occurrences(arr, seq):
    count = 0
    for i in range(len(arr) - len(seq) + 1):
        if np.array_equal(arr[i:i+len(seq)], seq):
            count += 1
    return count

occurrences = count_sequence_occurrences(arr, sequence)
print(occurrences)

#%%
"""Find the most frequent value in a NumPy array"""

import numpy as np

# Sample numpy array
arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5])

# Function to find the most frequent value
def most_frequent_value(arr):
    values, counts = np.unique(arr, return_counts=True)
    index = np.argmax(counts)
    return values[index]

most_frequent = most_frequent_value(arr)
print(most_frequent)

#%%
"""Combining a one and a two-dimensional NumPy Array"""

import numpy as np

# One-dimensional array
arr1 = np.array([1, 2, 3])

# Two-dimensional array
arr2 = np.array([
    [4, 5, 6],
    [7, 8, 9]
])

# Function to combine one and two-dimensional arrays
def combine_arrays(arr1, arr2):
    return np.vstack((arr1, arr2))

combined_array = combine_arrays(arr1, arr2)
print(combined_array)

#%%
"""C. 
Develop algorithms and Write a program using PYTHON to determine the roots of a 
quadratic equation using i)bisection method algorithm , ii) regular falsi iii)Newton 
Raphson method and iv) secant method. Determine the time complexity of your program
 NB All data must be supplied by the user
• Equation
• Lower/upper limit
• Error tolerance
• Iterations
"""
import numpy as np
import time

# Quadratic function
def quadratic_function(a, b, c):
    return lambda x: a*x**2 + b*x + c

# Input from user
def get_user_input():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    lower_limit = float(input("Enter lower limit: "))
    upper_limit = float(input("Enter upper limit: "))
    tolerance = float(input("Enter error tolerance: "))
    max_iterations = int(input("Enter maximum iterations: "))
    return a, b, c, lower_limit, upper_limit, tolerance, max_iterations

#%%
#ii) Regular Falsi Method
def regular_falsi_method(func, a, b, tol, max_iter):
    start_time = time.time()
    for i in range(max_iter):
        c = b - (func(b) * (a - b)) / (func(a) - func(b))
        if func(c) == 0 or abs(func(c)) < tol:
            end_time = time.time()
            return c, end_time - start_time
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    end_time = time.time()
    return c, end_time - start_time

a, b, c, lower_limit, upper_limit, tolerance, max_iterations = get_user_input()
func = quadratic_function(a, b, c)
root, time_taken = regular_falsi_method(func, lower_limit, upper_limit, tolerance, max_iterations)
print(f"Regular Falsi Method: Root = {root}, Time taken = {time_taken:.6f} seconds")

#%%
#iii) Newton Raphson Method
def newton_raphson_method(func, dfunc, x0, tol, max_iter):
    start_time = time.time()
    for i in range(max_iter):
        x1 = x0 - func(x0) / dfunc(x0)
        if abs(x1 - x0) < tol:
            end_time = time.time()
            return x1, end_time - start_time
        x0 = x1
    end_time = time.time()
    return x1, end_time - start_time

def derivative_of_quadratic(a, b):
    return lambda x: 2*a*x + b

a, b, c, lower_limit, upper_limit, tolerance, max_iterations = get_user_input()
func = quadratic_function(a, b, c)
dfunc = derivative_of_quadratic(a, b)
initial_guess = (lower_limit + upper_limit) / 2
root, time_taken = newton_raphson_method(func, dfunc, initial_guess, tolerance, max_iterations)
print(f"Newton Raphson Method: Root = {root}, Time taken = {time_taken:.6f} seconds")

#%%
#iv) Secant Method
def secant_method(func, x0, x1, tol, max_iter):
    start_time = time.time()
    for i in range(max_iter):
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        if abs(x2 - x1) < tol:
            end_time = time.time()
            return x2, end_time - start_time
        x0, x1 = x1, x2
    end_time = time.time()
    return x2, end_time - start_time

a, b, c, lower_limit, upper_limit, tolerance, max_iterations = get_user_input()
func = quadratic_function(a, b, c)
root, time_taken = secant_method(func, lower_limit, upper_limit, tolerance, max_iterations)
print(f"Secant Method: Root = {root}, Time taken = {time_taken:.6f} seconds")

#%%
