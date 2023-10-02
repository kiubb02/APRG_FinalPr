# Python file for Algorithm 2
class QuickHull:
    def __init__(self, points, modus):
        self.points = points
        self.hull = []
        # we need that to know if we will use visualization or not
        self.modus = modus

    def find_hull(self):
        if len(self.points) < 3:
            return self.points

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

        return self.hull

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

