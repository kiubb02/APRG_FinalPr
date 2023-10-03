#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:35:29 2023

@author: apatecpetschnig
"""
import csv
import time
import numpy as np
from algorithms.giftwrapping import GiftWrapping
from tabulate import tabulate

def main():
    # Initialize an empty list to store computation times per iteration
    benchmarks = []

    # Generate random points for testing with i*10000 points per iteration
    for i in range(1, 5):
        # Generate i*10000 random points
        num_points = i * 100
        points = np.random.rand(num_points, 2).tolist()

        print(f"Generated {num_points} random points.")  # print number of random points generated

        # Create JarvisMarch object using generated points
        jm = GiftWrapping(points)

        # Start the timer
        start_time = time.time()

        # Compute convex hull
        hull = jm.convex_hull()

        print(f"Convex hull points: {hull}")  # print convex hull points

        # Stop the timer
        end_time = time.time()

        # Calculate elapsed time
        elapsed_time = end_time - start_time

        print(f"Time taken: {elapsed_time} seconds.")  # print time taken for computation

        # Add the number of points and elapsed time to benchmarks list
        benchmarks.append([num_points, elapsed_time]) 

    # Write benchmarks to a CSV file
    with open('benchmarks_million_points.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(["Number of points", "Time taken"])
        # Write data rows
        writer.writerows(benchmarks)

    # Print the table in console
    print(tabulate(benchmarks, headers=["Number of points", "Time taken"], tablefmt='pretty'))

if __name__ == "__main__":
    main()