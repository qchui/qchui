"""
输入两个链表，找出它们的第一个公共结点。

如果两个链表长度一样，则正常遍历，找到相同的或者不存在。
如果两个链表长度不同，则首先短的遍历结束后会从另一个链表开头开始遍历，
而当另一个节点遍历结束后从另一个链表头开始遍历时，这两个链表的差则会消除。
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # def FindFirstCommonNode(self, pHead1, pHead2):
    #     if pHead1==pHead2:
    #         return pHead1
    #     p1=pHead1
    #     p2=pHead2
    #     while p2:
    #         while p1:
    #             if p1.next==p2:
    #                 return p2
    #             p1=p1.next
    #         p2=p2.next
    #     return None
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = p1.next if p1 != None else pHead2
            p2 = p2.next if p2 != None else pHead1
        return p1