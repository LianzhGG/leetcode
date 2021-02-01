"""
水位上升的游泳池中游泳
LeetCode index：778
"""
from typing import List


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

    def calculate(self, grid: List[List[int]], unable_value: int):
        unable_node: List[List[int]] = []
        unable_node[1][2] = 1
