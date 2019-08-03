# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number<1:
            return 0
        list = [1,2]
        while number > 1:
            list[0], list[1] = list[1], list[0] + list[1]
            number -= 1
        return list[0]
print(Solution().jumpFloor(1))