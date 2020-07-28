MoutainArry = [1, 3, 5, 7, 5, 4, 1]


class MountainArryInterfacne:
    def __init__(self, arry_list):
        self.arry_list = arry_list

    def get(self, index):
        return self.arry_list[index]

    def length(self):
        return len(self.arry_list)


class Solution:

    def getMoutainArry(self, target):
        # 找峰值
        arr = MountainArryInterfacne(MoutainArry)
        length = arr.length()
        top_index = length - 1
        i = 0
        j = length - 1
        while i+1 < j:
            # 二分法找峰值
            mid = i + ((j-i) >> 1)
            pri_value = arr.get(mid - 1)
            value = arr.get(mid)
            back_value = arr.get(mid + 1)
            if pri_value < value > back_value:
                top_index = mid
                break
            elif pri_value < value:
                # up
                i = mid
            else:
                # down
                j = mid
        # print("峰值为：", arr.get(top_index), "下标为：", top_index)
        l_index = 0
        r_index = top_index
        temp = -1
        while l_index + 1 < r_index:
            mid_index = int((l_index+r_index)/2)
            mid_value = arr.get(mid_index)
            if mid_value == target:
                temp = mid_index
                break
            elif mid_value > target:
                r_index = mid_index
                continue
            else:
                l_index = mid_index
                continue
        if temp >= 0:
            return temp
        else:
            l_index = top_index
            r_index = length - 1
            while l_index + 1 < r_index:
                mid_index = int((l_index + r_index) / 2)
                mid_value = arr.get(mid_index)
                if mid_value == target:
                    temp = mid_index
                    break
                elif mid_value > target:
                    l_index = mid_index
                    continue
                else:
                    r_index = mid_index
                    continue
        if temp >= 0:
            return temp
        else:
            # 二分法到最后左右两边第一个位置跳不出来，后续再优化
            if target == arr.get(0):
                temp = 0
            elif target == arr.get(length-1):
                temp = length - 1
            elif target == arr.get(top_index):
                temp = top_index
        if temp >= 0:
            return temp
        else:
            return -1


for i in MoutainArry:
    target = i
    print("要找的数值", i)
    a = Solution()
    print("下标为：", a.getMoutainArry(target))
# a.getMoutainArry(target)

