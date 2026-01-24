
# mean-variance-standard-deviation-calculator

## Overview
This project implements a Python function `calculate()` that computes statistical measures on a 3x3 matrix derived from a list of nine numbers. 
The function returns a dictionary containing the mean, variance, standard deviation, maximum, minimum, and sum of the numbers. 
Each statistic is calculated across columns, rows, and the flattened matrix.

## Requirements:
- Input list must contain exactly nine numbers; otherwise, a ValueError is raised.
- Uses NumPy for calculations.

**Example Usage:**
from mean_var_std import calculate

result = calculate([1,2,3,4,5,6,7,8,9])
print(result)

Expected Output:
{
  'mean': [[2.0, 5.0, 8.0], [1.0, 4.0, 7.0], 5.0],
  'variance': [[0.666..., 0.666..., 0.666...], [0.666..., 0.666..., 0.666...], 6.666...],
  'standard deviation': [[0.816..., 0.816..., 0.816...], [0.816..., 0.816..., 0.816...], 2.581...],
  'max': [[3, 6, 9], [7, 8, 9], 9],
  'min': [[1, 4, 7], [1, 2, 3], 1],
  'sum': [[6, 15, 24], [6, 15, 24], 45]
}

## How to Run:
1. Ensure Python 3 and NumPy are installed.
2. Save `mean_var_std.py` in a folder.
3. Open a terminal in that folder.
4. Run the file or import the function in another script.

***This project was completed as part of the freeCodeCamp Data Analysis with Python certification and demonstrates practical use of NumPy for numerical calculations and structuring results in a dictionary.***
