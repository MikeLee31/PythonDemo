# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 不难，提取到列表排序，关键是构造AC要求的链表
        num =[]
        l1 = list1
        l2 = list2
        if l1 is not None:
            while(l1 is not None):
                num.append(l1.val)
                l1 = l1.next
        if l2 is not None:
            while (l2 is not None):
                num.append(l2.val)
                l2 = l2.next
        print(num)
        num.sort()
        # 这边反转后容易链接
        num.reverse()
        if len(num) != 0:
            l = ListNode(num[0], None)
            for i in range(1, len(num)):
                l = ListNode(num[i], l)
            return l
        else:
            return None




