"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

分析这道题时，最先想到的解题思路是：两个栈分别负责入栈和出栈，
当需要出栈时，将所有数据转移到负责出栈的栈中，再进行出栈操作；
当需要入栈时，将所有数据转移到负责入栈的栈中，再进行出栈操作。这样可以利用两个栈实现数据的先入先出的特性。
"""
class Solution:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, node):
        while self.stackOut:
            self.stackIn.append(self.stackOut.pop(-1))
        self.stackIn.append(node)

    def pop(self):
        while self.stackIn:
            self.stackOut.append(self.stackIn.pop(-1))
        return self.stackOut.pop(-1)
