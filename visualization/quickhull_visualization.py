import matplotlib.pyplot as plt
import time
from tkinter import messagebox


class VisualizationQuickhull:
    def __init__(self, points):
        self.points = points
        self.fig, self.ax = plt.subplots()
        self.sc = self.ax.scatter(*zip(*points))
        self.anim = None

    def visualize_quickhull(self, hull):
        # Record time taken
        start_time = time.time()

        if len(self.points) < 3:
            end_time = time.time()
            elapsed_time = end_time - start_time
            messagebox.showinfo("Results", f"Convex Hull: {hull}\nTime taken: {elapsed_time} seconds.")
            return

        # Plot the input points
        self.ax.scatter(*zip(*self.points), color='blue', label='Data Points')
        self.ax.legend()

        # Animate the QuickHull algorithm
        self._animate_quickhull(hull)

        # Record the time taken and display the convex hull in a message box
        end_time = time.time()
        elapsed_time = end_time - start_time
        messagebox.showinfo("Results", f"Convex Hull: {hull}\nTime taken: {elapsed_time} seconds.")
        plt.show()

    def _animate_quickhull(self, hull):
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
