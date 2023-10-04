# Python file for Algorithm 2
# need this to print the results and the graph and al
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from helpers.geometry import Geometry


class QuickHull:
    def __init__(self, points, visualize):
        self.points = points
        self.hull = []
        # we need that to know if we will use visualization or not
        self.visualize = visualize  # is either True or False
        # everything we need for the plot
        self.fig, self.ax = plt.subplots()
        self.sc = self.ax.scatter(*zip(*self.points))
        self.anim = None

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
            if Geometry.orientation_qh(leftmost, rightmost, point) == -1:
                left_set.append(point)
            elif Geometry.orientation_qh(leftmost, rightmost, point) == 1:
                right_set.append(point)

        # Recursively find convex hulls of the two sets
        self.quickhull(leftmost, rightmost, left_set)
        self.quickhull(rightmost, leftmost, right_set)

        end_time = time.time()
        elapsed_time = end_time - start_time

        # see if we want to visualize or not
        if self.visualize:
            print("Plot the Animation")

        messagebox.showinfo("Results", f"Convex Hull: {self.hull}\nTime taken: {elapsed_time} seconds.")

    def quickhull(self, p1, p2, point_set):
        if not point_set:
            return

        max_distance = -1
        farthest_point = None

        for point in point_set:
            d = Geometry.distance(p1, p2, point)
            if d > max_distance:
                max_distance = d
                farthest_point = point

        self.hull.append(farthest_point)
        point_set.remove(farthest_point)

        left_set = []
        right_set = []
        for point in point_set:
            if Geometry.orientation_qh(p1, farthest_point, point) == 1:
                left_set.append(point)
            elif Geometry.orientation_qh(farthest_point, p2, point) == 1:
                right_set.append(point)

        self.quickhull(p1, farthest_point, left_set)
        self.quickhull(farthest_point, p2, right_set)

    ##############################################################
    #                                                            #
    #                      HELPER FUNCTIONS                      #
    #                                                            #
    ##############################################################

    """"

    def plot_hull(self):
        lines = []
        for i in range(len(self.hull) - 1):
            lines.append([(self.hull[i][0], self.hull[i+1][0]), (self.hull[i][1], self.hull[i+1][1])])
        lines.append([(self.hull[-1][0], self.hull[0][0]), (self.hull[-1][1], self.hull[0][1])])

        self.lines = [self.ax.plot(line[0], line[1], color='red')[0] for line in lines]

        self.sc = self.ax.scatter(*zip(*self.points), color='blue', label='Data Points')
        self.ax.legend()

        plt.draw()
        plt.pause(0.001)

        for i in range(len(self.hull)):
            self.sc.set_offsets(self.hull[i])
            for line in self.lines:
                line.set_visible(True)
            plt.draw()

            # Wait for user input to navigate the animation
            while True:
                event = plt.waitforbuttonpress()
                if event:
                    break

        plt.show()
        
    """
