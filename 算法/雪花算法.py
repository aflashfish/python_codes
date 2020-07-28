"""
位运算过程
正数反码：与原码相同
负数反码：符号位为“1”，数值位按位 取反。
正数补码：与原码相同
负数补码：求反加一
所有参与运算的都是以补码形式进行的 结果也是补码 因此也需要将补码转换成为原码的形式存在


结果也是补码，所以必须要转换成为原码
分为两种情况：
1.如果最高为为1 即为负数 那么最高位不变 其他按位取反，
最后加一 和前边补码转原码是一样的
2.最高为是0,不用转化

-64的原码：
1000 0000 0100 0000
-64的反码：
1111 1111 1011 1111
-64的补码：
1111 1111 1100 0000

-1的原码：
1000 0000 0000 0001
-1的反码：
1111 1111 1111 1110
-1的补码
1111 1111 1111 1111

两补码异或：
1111 1111 1100 0000
1111 1111 1111 1111
结果补码：
0000 0000 0011 1111
反码：
0000 0000 0011 1111
原码：
1000 0000 0011 1110
"""

# ==========================================================================
"""
雪花算法：
符号位：         1位
时间戳：         41位
工作机器id：     10位
循环序列位：     12位          // 一毫秒内生产不同的id，12位最多4095，多出来的等待下一毫秒

可以根据实际情况优化工作机器位和序列位
"""

"""
例子：
服务目前QPS10万，预计几年之内会发展到百万。
当前机器三地部署，上海，北京，深圳都有。
当前机器10台左右，预计未来会增加至百台。

百万吞吐量的访问，每毫秒为千级的访问量，10台机器，每台的承担量为百级别；
机器在3地部署，可以用3位进行区域识别，最多可以识别8个地区；//也可以更改
机器识别号用7位进行计算识别；
"""
import time


WORKER_ID_BITS = 7
DATACENTER_ID_BITS = 3
SEQUENCE_BITS = 12


# 最大取值计算
MAX_WORKER_ID = -1 ^ (-1 << WORKER_ID_BITS)  # 2**7-1 0b1111111
MAX_DATACENTER_ID = -1 ^ (-1 << DATACENTER_ID_BITS)  # 0b111

# 移位偏移计算
WORKER_ID_SHIFT = SEQUENCE_BITS                         # 向左移12位
DATACENTER_ID_SHIFT = WORKER_ID_BITS + SEQUENCE_BITS    # 向左移7+12位
TIMESTAMP_LEFT_SHIFT = DATACENTER_ID_BITS + WORKER_ID_BITS + SEQUENCE_BITS

# 序号循环掩码
SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS)

# Twitter元年时间戳
TWEPOCH = 1288834974657

print(int(int(time.time())/60/60/24/365))


class IdWorker:
    """
    用于生成ids
    """
    def __init__(self, datacenter_id, worker_id, sequence=0):
        """
        初始化
        :param datacenter_id: 数据中心（机器区域）ID
        :param worker_id: 机器ID
        :param sequence: 序号
        """
        # check
        if datacenter_id > MAX_DATACENTER_ID or datacenter_id < 0:
            raise ValueError("机器区域id超过限价：0 < value < 8")

        if worker_id > MAX_WORKER_ID or worker_id < 0:
            raise ValueError("机器id超过限价：0 < value < 128")

        self.datacenter_id = datacenter_id
        self.worker_id = worker_id
        self.sequence = sequence

        self.last_timestamp = -1  # 上次计算的时间戳

    def _get_timestamp(self):
        """
        生成时间戳
        :return:
        """
        return int(time.time() * 1000)

    def get_id(self):
        """
        生成id
        :return:
        """
        timestamp = self._get_timestamp()

        # 时间回拨处理
        if timestamp < self.last_timestamp:
            raise ValueError("时间回拨异常")

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & SEQUENCE_MASK
            if self.sequence == 0:
                timestamp = self._til_next_millis(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        new_id = (timestamp - TWEPOCH) << TIMESTAMP_LEFT_SHIFT | (self.datacenter_id << DATACENTER_ID_SHIFT) | \
                 (self.worker_id << WORKER_ID_SHIFT) | self.sequence

        return new_id

    def _til_next_millis(self, last_timestamp):
        """
        等到下一毫秒
        """
        timestamp = self._get_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._get_timestamp()
        return timestamp


if __name__ == '__main__':
    worker = IdWorker(1, 2, 0)
    print(worker.get_id())
    worker = IdWorker(2, 3, 0)
    print(worker.get_id())
