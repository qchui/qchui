"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'
表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，
但是与"aa.a"和"ab*a"均不匹配
"""


# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # 递归终止条件
        if s == pattern: return True
        if not pattern: return False
        # 判断第二个字符是否为 *
        if len(pattern) > 1 and pattern[1] == '*':
            # 判断首字符是否相等，不要忘记 . 的情况
            if s and (pattern[0] == s[0] or pattern[0] == '.'):
                # 相等的情况下，三种匹配模式
                return self.match(s[1:], pattern[2:]) \
                       or self.match(s, pattern[2:]) \
                       or self.match(s[1:], pattern)
            else:
                # 不等时，只能将pattern后移，继续判断
                return self.match(s, pattern[2:])
        # 第二个字符不为 *，直接对首字符进行比较
        elif s and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])

        return False
