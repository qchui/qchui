"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
# -*- coding:utf-8 -*-
class Solution:
    def theMax(self, str1, str2):
        '''定义字符串比较函数'''
        return str1 if str1+str2 > str2+str1 else str2

    def PrintMinNumber(self, numbers):
        """使用冒泡进行排序(把最大的放最后)"""
        string = [str(num) for num in numbers]
        count = len(string) - 1
        while count > 0:
            for i in range(len(string)-1):
                if self.theMax(string[i], string[i+1]) == string[i]:
                    string[i],string[i+1]=string[i+1],string[i]
            count -= 1
        string = ''.join(string)
        return string


print(Solution().PrintMinNumber([3334,34,3,34]))
