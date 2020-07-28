"""
小王来到了游乐园，她玩的第一个项目是模拟推销员。有一个二维平面地图，
其中散布着 N 个推销点，编号 0 到 N-1，不存在三点共线的情况。
每两点之间有一条直线相连。游戏没有规定起点和终点，
但限定了每次转角的方向。首先，小王需要先选择两个点分别作为起点和终点，
然后从起点开始访问剩余 N-2 个点恰好一次并回到终点。访问的顺序需要满足一串给定的长度为 N-2
由 L 和 R 组成的字符串 direction，表示从起点出发之后在每个顶点上转角的方向。
据这个提示，小王希望你能够帮她找到一个可行的遍历顺序，输出顺序下标
（若有多个方案，输出任意一种）。可以证明这样的遍历顺序一定是存在的。

"""


"""
=======================  解题思路解析 ==========================
1、找出最左边的点，作为开始的点，也就是横坐标为最小的点
2、根据下一次的方向来选择点：
    （1）如果是要走左边：
        那么就要找到最右边的点，开始的点到该点的向量作为第一步，那么下一步往左走的时候，所有点
        都在这个向量的左边，就可以让下一步走下去，可以迭代完成所有的点；
    （2）如果是要走右边：
        那么就要找到最右边的点，这样形成的向量后，所有的点在该向量的右边；     
3、判断最右边的点和最左边的点的方法：
    根据向量的乘积正负，可以判断出点是在最左边或者是最右边；
    正：则在右边
    负：在左边
    
4、 nxt = -1是初始状态，在迭代寻找符合点的时候，获取剩余的点的第一个点的值作为参考向量，后面的遍历不会判断到；
    （1）如果要找左边，那么向量乘积应该为负；
         在判断中，为正的，说明这个点在参考向量的右边，反之在左边；
         当在左边的时候，把根点和该点形成新的一个参考向量，相当于往左移一个点；
         再去判断剩余的点，遍历完所有的点后，最后一次为负的，则是在最左边；
         就把该点的位置告诉nxt。下一步就是往这个点走！
    （2）如果找右边，就和（1）相反的走
    （3）当迭代完成所有的点后，会剩余一个点没办法遍历完，这个点就是结束点，直接加进路径最后一步就可以了。
    
"""

points = [[1, 1], [1, 4], [3, 2], [2, 1]]
direction = "LL"


class Solution:

    def sub(self, a, b):
        # 返回a,b两点的向量
        return [a[0]-b[0], a[1]-b[1]]

    def cross(self, a, b):
        # 两向量的乘积
        return a[0] * b[1] + a[1] * b[0]

    def visitOrder(self, points, direction):
        n = len(points)
        # 记录哪些点被使用过
        used = [False] * n
        # 记录返回结果
        order = []

        # 查找最左边的位置作为开始点
        start = 0
        for i in range(n):
            if points[i][0] < points[start][0]:
                start = i
        used[start] = True
        order.append(start)

        for i in direction:
            nxt = -1
            if i == "L":
                # 转向方向为 L，选择相对方向最右的点
                # 遍历没有使用的点
                for j in range(n):
                    if not used[j]:
                        if nxt == -1 or self.cross(self.sub(points[nxt], points[start]),
                                                   self.sub(points[j], points[start])) < 0:
                            nxt = j

            else:
                # 转向方向为 L，选择相对方向最右的点
                # 遍历没有使用的点
                for j in range(n):
                    if not used[j]:
                        if nxt == -1 or self.cross(self.sub(points[nxt], points[start]),
                                                   self.sub(points[j], points[start])) > 0:
                            nxt = j

            # 返回结果加入选择的点，更新下一次转向的起点
            used[nxt] = True
            order.append(nxt)
            start = nxt

        # 添加最后一个剩余点
        for i in range(0, n):
            if not used[i]:
                order.append(i)
        return order


if __name__ == "__main__":
    s = Solution()
    ret = s.visitOrder(points, direction)
    print(ret)
