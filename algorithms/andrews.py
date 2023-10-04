# need this to print the results and the graph and al
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import time
from helpers.geometry import Geometry


class AndrewsAlgorithm:
    def __init__(self, points, visualize):
        self.points = sorted(set(points))  # Remove duplicates and sort the points
        self.convex_hull = []
        self.visualize = visualize
        self.fig, self.ax = plt.subplots()
        self.sc = self.ax.scatter(*zip(*self.points))
        self.anim = None

    def convex_hull_andrew(self):
        start_time = time.time()
        n = len(self.points)
        if n < 3:
            end_time = time.time()
            elapsed_time = end_time - start_time
            self.convex_hull = self.points
            messagebox.showinfo("Results", f"Convex Hull: {self.convex_hull}\nTime taken: {elapsed_time} seconds.")
            return

        lower_hull = []
        for p in self.points:
            while len(lower_hull) >= 2 and Geometry.orientation_andrews(lower_hull[-2], lower_hull[-1], p) != -1:
                lower_hull.pop()
            lower_hull.append(p)

        upper_hull = []
        for p in reversed(self.points):
            while len(upper_hull) >= 2 and Geometry.orientation_andrews(upper_hull[-2], upper_hull[-1], p) != -1:
                upper_hull.pop()
            upper_hull.append(p)

        self.convex_hull = lower_hull[:-1] + upper_hull[:-1]

        end_time = time.time()
        elapsed_time = end_time - start_time

        if self.visualize == "visual":
            print("Plot the Animation")
            self._animate_andrews(self.convex_hull)

        messagebox.showinfo("Results", f"Convex Hull: {self.convex_hull}\nTime taken: {elapsed_time} seconds.")

        print("Convex Hull:")
        for point in self.convex_hull:
            print(point)

        return

    def _animate_andrews(self, hull):
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
