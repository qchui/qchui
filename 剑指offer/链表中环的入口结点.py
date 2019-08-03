'''
剑指offer python版 链表中环的入口结点
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

//先说个定理：两个指针一个fast、一个slow同时从一个链表的头部出发
//fast一次走2步，slow一次走一步，如果该链表有环，两个指针必然在环内相遇
//此时只需要把其中的一个指针重新指向链表头部，另一个不变（还在环内），
//这次两个指针一次走一步，相遇的地方就是入口节点。

'''

class Solution:
    def EntryNodeOfLoop(self, pHead):
        pFast = pHead
        pSlow = pHead
        while pFast != None and pFast.next != None:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                break
        if pFast == None or  pFast.next == None:
            return None
        pFast = pHead
        while (pFast != pSlow):
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast
