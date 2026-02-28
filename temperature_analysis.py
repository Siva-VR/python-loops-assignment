"""
=========================================================
Temperature & NumPy Data Analysis Assignment
Author: Your Name
Course: Python Programming
Description:
This script completes three tasks:

1. Temperature data processing using NumPy arrays
2. Array shape and statistical analysis
3. Performance comparison between NumPy arrays and Python lists

All operations use NumPy vectorized methods (no loops where restricted).
=========================================================
"""

import numpy as np

import time


# =========================================================
# Task 1: Temperature Data Processing
# =========================================================
print("========== Task 1: Temperature Processing ==========\n")

# Create NumPy array of Celsius temperatures
temps_celsius = np.array([22, 25, 28, 24, 26])

# Convert Celsius to Fahrenheit
temps_fahrenheit = temps_celsius * 1.8 + 32

# Display results
print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)

# Calculate average Fahrenheit temperature (rounded to 1 decimal place)
avg_fahrenheit = np.round(np.mean(temps_fahrenheit), 1)
print("Average Fahrenheit:", avg_fahrenheit)


# =========================================================
# Task 2: Array Shape and Statistics
# =========================================================
print("\n========== Task 2: Array Shape & Statistics ==========\n")

# Create NumPy array of test scores
scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

# Print shape and total elements
print("Shape:", scores.shape)
print("Total elements:", scores.size)

# Calculate statistics
highest_score = np.max(scores)
lowest_score = np.min(scores)
score_range = highest_score - lowest_score

# Display statistics
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Range:", score_range)


# =========================================================
# Task 3: Performance Comparison (NumPy vs Python List)
# =========================================================
print("\n========== Task 3: Performance Comparison ==========\n")

# Create NumPy array and Python list
numpy_array = np.arange(1, 50001)
python_list = list(range(1, 50001))

# NumPy sum timing
start_numpy = time.time()
numpy_sum = np.sum(numpy_array)
end_numpy = time.time()
numpy_time = end_numpy - start_numpy

# Python sum timing
start_python = time.time()
python_sum = sum(python_list)
end_python = time.time()
python_time = end_python - start_python

# Calculate speed difference
speed_ratio = python_time / numpy_time

# Display results
print("NumPy sum:", numpy_sum)
print("Python sum:", python_sum)
print("NumPy time:", format(numpy_time, ".4f"), "seconds")
print("Python time:", format(python_time, ".4f"), "seconds")
print("NumPy is", round(speed_ratio, 1), "x faster")


print("\n========== End of Assignment ==========")