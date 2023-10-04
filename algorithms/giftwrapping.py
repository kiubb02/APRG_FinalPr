#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:33:54 2023

@author: apatecpetschnig
"""

from helpers.geometry import Geometry
from tkinter import messagebox
import time
import matplotlib.pyplot as plt


class GiftWrapping:
    def __init__(self, points, visualize):
        # Initialize the object with a list of points and the number of points
        self.points = points
        self.n = len(points)
        self.visualize = visualize
        self.fig, self.ax = plt.subplots()
        self.sc = self.ax.scatter(*zip(*self.points))
        self.anim = None

    def convex_hull(self):
        # record time taken
        start_time = time.time()

        """
        find convex hull
        """
        # If there are less than 3 points, there is no polygon can be formed, so return
        if self.n < 3:
            return

        # Determine the leftmost point
        left_most = Geometry.left_index(self.points)

        # Initialize an empty list to store the points of the hull
        hull = []

        # Start from the leftmost point
        p = left_most
        q = None

        # Loop forever
        while True:
            # Add the current point to the hull
            hull.append(self.points[p])

            # Let q be the next point in the list after p
            q = (p + 1) % self.n

            # For every point in the set
            for r in range(self.n):
                # If the ordered triplet (point[p], point[q], point[r]) makes a counter-clockwise turn
                if Geometry.orientation(self.points[p], self.points[q], self.points[r]) == 2:
                    # Update q to be r
                    q = r

            # Let's p to be q for our next loop
            p = q

            # Break out of the loop when we're back to the start
            if p == left_most:
                break

        # Return the ordered list of points in the convex hull
        # return hull

        end_time = time.time()
        elapsed_time = end_time - start_time

        if self.visualize == "visual":
            print("Plot the Animation")
            self._animate_giftwrapping(hull)

        # since we want to create a report - get a csv which will always be appended

        # print the convex hull in a message box
        messagebox.showinfo("Results", f"Convex Hull: {hull}\nTime taken: {elapsed_time} seconds.")
        print(hull)

    def _animate_giftwrapping(self, hull):
        if not hull:
            return

        for i in range(len(hull)):
            if i == len(hull) - 1:
                # Draw the last edge connecting the last point to the first point
                x_edge = [hull[i][0], hull[0][0]]
                y_edge = [hull[i][1], hull[0][1]]
            else:
                # Draw edges between consecutive points in the hull
                x_edge = [hull[i][0], hull[i + 1][0]]
                y_edge = [hull[i][1], hull[i + 1][1]]

            self.ax.plot(x_edge, y_edge, color='red')
            plt.pause(0.5)  # Pause briefly to show each step of the algorithm
