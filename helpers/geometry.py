#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:30:04 2023

@author: apatecpetschnig
"""


class Geometry:

    @staticmethod
    def left_index(points):
        """
        Find the leftmost point
        """
        # Initialize left_most_index as the index of first point
        left_most_index = 0

        # Cycle through the points starting from the second one
        for i in range(1, len(points)):
            # If the x-coordinate of the current point is less than the left_most_index point's x-coordinate
            if points[i][0] < points[left_most_index][0]:
                # Update the left_most_index to current point's index
                left_most_index = i
            # If the x-coordinates are equal, compare y-coordinates
            elif points[i][0] == points[left_most_index][0]:
                # If the y-coordinate of the current point is greater than the left_most_index point's y-coordinate
                if points[i][1] > points[left_most_index][1]:
                    # Update the left_most_index to current point's index
                    left_most_index = i

        # Return the index of leftmost point
        return left_most_index

    @staticmethod
    def orientation(p, q, r):
        """
        Find orientation of ordered triplet (p, q, r)
        """
        # Calculate cross product of vectors formed by points p, q and q, r
        value = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        # If value is 0, points are collinear
        if value == 0:
            return 0
        # If value is greater than 0, points are in clockwise direction
        elif value > 0:
            return 1
        # If value is less than 0, points are in counterclockwise direction
        else:
            return 2
