"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，
使用GetMedian()方法获取当前读取数据的中位数。
"""
from heapq import *    # 利用python的heapq库,来实现堆
class Solution:
    def __init__(self):
        self.small = []
        self.large = []
    def Insert(self, num):
        # write code here
        small,large = self.small,self.large
        heappush(small,-heappushpop(large,-num))
        if len(large) < len(small):
        # 这样就保持了大顶堆和小顶堆元素个数的相对稳定性，在取中位数的时候也方便。
            heappush(large,-heappop(small))
    def GetMedian(self,n=1):
        # write code here
        small,large = self.small,self.large
        if len(large) > len(small):
            return float(-large[0])
        return (small[0] - large[0]) / 2.0