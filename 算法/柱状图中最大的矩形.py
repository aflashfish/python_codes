"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。
每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""
from typing import List

rectangle_list = [2, 1, 5, 6, 2, 3]


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        _heard = 0
        area_list = []
        max_value = 0
        for i in range(len(heights)):
            if heights[i] == 0:
                continue
            temp_list = []
            _heard = heights[i]
            # print("===========每次第一个", heights[i])
            temp_list.append(_heard)
            for j in range(i+1, len(heights)):
                if heights[j] == 0:
                    break
                if heights[j] <= _heard:
                    _heard = heights[j]
                temp_list.append(_heard)
                # print("添加", _heard)
            for k in range(len(temp_list)):
                area_list.append(temp_list[k] * (k+1))
        if area_list:
            max_value = max(area_list)
        return max_value


if __name__ == "__main__":
    heights = eval(input())
    max_value = Solution().largestRectangleArea(heights)
    print(max_value)
