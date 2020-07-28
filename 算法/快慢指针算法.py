from typing import List
nums = [1, 3, 4, 2, 2]

"""
顺序：
1       slow -> nums[0] = 1      fast -> nums[nums[0]] -> nums[1] -> 3
2       slow -> nums[1] -> 3     fast -> nums[nums[3]] -> nums[2] -> 4
3       slow -> nums[3] -> 2     fast -> nums[nums[4]] -> nums[2] -> 4
4       slow -> nums[2] -> 4     fast -> nums[nums[4]] -> nums[2] -> 4
"""



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # node = index of nums
        # node.next = nums[node]
        # node.next.next = nums[nums[node]]
        slow = nums[0]         # 先走一步
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]  # 曾经犯的一个错误，以为这里会固定地在环入口，值相同的那个点相遇
        root = 0                     # 其实它们可以在环上任何一个node相遇，这里就是任何一个数组的下标index
        while root != slow:
            root = nums[root]
            slow = nums[slow]
        return slow
# 回到循环结束的上一步
# nums[proot] == nums[pslow]
# The last slow = nums[proot] and this value at least has two slot in the array


ret = Solution().findDuplicate(nums)
print(ret)
