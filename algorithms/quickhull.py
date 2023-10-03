# Python file for Algorithm 2
# need this to print the results and the graph and al
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

class QuickHull:
    def __init__(self, points, visualize):
        self.points = points
        self.hull = []
        # we need that to know if we will use visualization or not
        self.visualize = visualize  # is either True or False
        # everything we need for the plot
        # self.fig = plt.figure()
        # self.ax = self.fig.add_subplot(111, projection='scatter')
        # self.sc = self.ax.scatter(*zip(*self.points))
        # self.anim = None

    def find_hull(self):
        start_time = time.time()

        if len(self.points) < 3:
            end_time = time.time()
            elapsed_time = end_time - start_time
            messagebox.showinfo("Results", f"Convex Hull: {self.hull}\nTime taken: {elapsed_time} seconds.")
            return

        # Find the leftmost and rightmost points
        leftmost = min(self.points)
        rightmost = max(self.points)

        # Split points into two sets
        left_set = []
        right_set = []
        for point in self.points:
            if self.orientation(leftmost, rightmost, point) == -1:
                left_set.append(point)
            elif self.orientation(leftmost, rightmost, point) == 1:
                right_set.append(point)

        # Recursively find convex hulls of the two sets
        self.quickhull(leftmost, rightmost, left_set)
        self.quickhull(rightmost, leftmost, right_set)

        end_time = time.time()
        elapsed_time = end_time - start_time

        # see if we want to visualize or not
        if self.visualize:
            print("Plot started")
            # self.plot_hull()

        messagebox.showinfo("Results", f"Convex Hull: {self.hull}\nTime taken: {elapsed_time} seconds.")

    def quickhull(self, p1, p2, point_set):
        if not point_set:
            return

        max_distance = -1
        farthest_point = None

        for point in point_set:
            d = self.distance(p1, p2, point)
            if d > max_distance:
                max_distance = d
                farthest_point = point

        self.hull.append(farthest_point)
        point_set.remove(farthest_point)

        left_set = []
        right_set = []
        for point in point_set:
            if self.orientation(p1, farthest_point, point) == 1:
                left_set.append(point)
            elif self.orientation(farthest_point, p2, point) == 1:
                right_set.append(point)

        self.quickhull(p1, farthest_point, left_set)
        self.quickhull(farthest_point, p2, right_set)

    ##############################################################
    #                                                            #
    #                      HELPER FUNCTIONS                      #
    #                                                            #
    ##############################################################

    @staticmethod
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # Collinear
        return 1 if val > 0 else -1  # Clockwise or Counterclockwise

    @staticmethod
    def distance(p1, p2, p3):
        return abs((p2[1] - p1[1]) * p3[0] + (p1[0] - p2[0]) * p3[1] + (p2[0] * p1[1] - p1[0] * p2[1])) / \
            ((p2[1] - p1[1]) ** 2 + (p1[0] - p2[0]) ** 2) ** 0.5

    """
    def plot_hull(self):
        def animate(i):
            if i < len(self.hull):
                self.sc.set_offsets(self.hull[i])
            return self.sc,

        self.anim = FuncAnimation(self.fig, animate, frames=len(self.hull), interval=500, repeat=False)
        plt.show()
    """
