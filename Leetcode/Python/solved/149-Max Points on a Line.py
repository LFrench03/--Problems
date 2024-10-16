#149 Max Points on a Line
'''
Given an array of points where points[i] = [xi, yi] represultents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.


Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:

1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.
'''
from collections import defaultdict
from math import atan2
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n == 1: return 1
        result = 2
        for i in range(n):
            d = defaultdict(int)
            for j in range(n):
                if i != j:
                    d[atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1
            result = max(result, max(d.values()) + 1)
        return result