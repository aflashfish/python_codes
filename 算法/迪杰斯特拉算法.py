"""
有初始位置的  有方向的  最小路径查找

"""
import numpy as np

"""
题目描述：游戏网站提供若干升级补丁，每个补丁大小不一，玩家要升级到最新版，如何选择下载哪些补丁下载量最小。

输入：     
第一行输入                第一个数为用户版本 第二个数为最新版本，空格分开
1000 1050

接着输入N行补丁数据       第一个数补丁开始版本 第二个数为补丁结束版本 第三个数为补丁大小，空格分开
1000 1020 50

1000 1030 70

1020 1030 15

1020 1040 30

1030 1050 40

1040 1050 20

样例输出：
1000->1020->1040->1050(100)
"""


def get_graph():
    """
    获取用户输入的各版本补丁大小
    :return:
    """
    ex_edi = 0
    next_edi = 0
    size = 0
    edi_list = []
    try:
        ex_edi, next_edi, size = input("请输入开始版本，结束版本，补丁大小，空格分开:").split(" ")
    except:
        pass
    while ex_edi:
        edi_list.append([ ex_edi, next_edi, size])
        try:
            ex_edi, next_edi, size = input("请输入开始版本，结束版本，补丁大小，空格分开:").split(" ")
        except:
            ex_edi = 0
    return edi_list


# 例子，edi_list用户输入了下面的信息
graph_01 = [
 ['1000', '1020', '50'],
 ['1000', '1030', '70'],
 ['1020', '1030', '15'],
 ['1020', '1040', '30'],
 ['1030', '1050', '40'],
 ['1040', '1050', '20']]


def get_arr(graph):
    """
    获取版本路径图
    :param graph:
    :return:
    """
    topic = []
    column = []
    for i in graph:
        topic.append(i[0])
        column.append(i[1])
    topic = topic + column
    topic = list(set(topic))
    topic.sort()
    length = len(topic)
    max = 10000
    arr = np.zeros(shape=[length, length])
    for i in range(length):
        for j in range(length):
            arr[i][j] = max
    for x in graph:
        for i in range(length):
            left_str = topic[i]
            for j in range(length):
                top_str = topic[j]
                if x[0] == left_str and x[1] == top_str:
                    arr[i][j] = int(x[2])
    return arr, length, topic


def dijkstra_get_minroute(start, end):
    # graph = get_graph()
    graph = graph_01
    arr, length, topic = get_arr(graph)
    flag = [0] * length
    weigth = [0] * length
    path = [0] * length
    for i in range(length):
        # 第一次进入，确定位置
        if topic[i] == start:
            flag[i] = 1
            weigth = arr[i]
        else:
            if topic[i] == end:
                break
            else:
                flag[i] = 1
                for j in range(i+1, length):
                    n = weigth[i]
                    # 有路
                    if arr[i][j] != max:
                        if arr[i][j]+n < weigth[j]:
                            weigth[j] = arr[i][j]+n
                            path[j] = i

    # 最小一共的下载量
    end_path_index = topic.index(end)
    min_size = weigth[end_path_index]
    path_note_str = ''
    now_path_index = end_path_index
    while now_path_index:
        fore_path_index = path[now_path_index]
        path_note_str = topic[now_path_index] + '--->' + path_note_str
        now_path_index = fore_path_index
    path_note_str = topic[0] + '--->' + path_note_str.rstrip("--->")
    print("一共最小下载量为：", min_size)
    print("路径为", path_note_str)
    return min_size, path_note_str


if __name__ == "__main__":
    dijkstra_get_minroute('1000', '1030')
