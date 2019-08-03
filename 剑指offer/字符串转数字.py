"""
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
+2147483647
    1a33
输出
2147483647       16 + 189 -   48 -59
    0
"""

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if s:
            if ord(s[0])==43:
                if ord(s[1])==48:
                    return 0
                else:
                    for n in s[1:]:
                        if ord(n) not in [48,49,50,51,52,53,54,55,56,57,58,59]:
                            return 0
                    return  s[1:]
            elif ord(s[0])==45:
                if ord(s[1]) == 48:
                    return 0
                else:
                    for n in s[1:]:
                        if ord(n) not in [48,49,50,51,52,53,54,55,56,57,58,59]:
                            return 0
                        return -int(s[1:])
            elif ord(s[0])==48:
                return 0

            elif ord(s[0]) in [49,50,51,52,53,54,55,56,57,58,59]:
                for n in s[0:]:
                    if ord(n) not in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]:
                        return 0
                return int(s)
            else:
                return 0

        else:
            return 0

print(Solution().StrToInt('+123'))
