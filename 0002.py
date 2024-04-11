# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Tuple,Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num3 = 0
        num4 = 0

        length1 = 0
        current = l1
        while current is not None :
            length1 += 1
            current = current.next
        for i in range(length1) :
            num1 = l1[i] * (10 ** i)
            num3 += num1
        print(num3)

        length2 = 0
        current = l2
        while current is not None :
            length2 += 1
            current = current.next
        for i in range(length2) :
            num2 = l2[i] * (10 ** i)
            num4 += num2
        print(num4)
        num = num3 + num4
        print(num)
        result_str = str(num)

        answer = ListNode(int(result_str[0]))
        # 这里 body 用来放到之后的 for 循环中不断获取之后的 next 节点
        print(answer.val)
        body = answer
        # 第一位 "7" 已经拿到了，接下来的范围就是第二位、也就是字符串的索引 1 开始
        for i in range(1, len(result_str)) :
            # 继续下一位 ListNode 的定义
            temp = ListNode(int(result_str[i]))
            # 如果不是最后一位的话，该 ListNode 的 next 就是下一位的 ListNode
            if i < len(result_str) - 1 :
                temp.next = ListNode(int(result_str[i + 1]))
            # 刚定义完的 ListNode 就是我们结果的 next
            body.next = temp
            # 为了让结果的每一位相连，将下一位赋值给 body，以在循环中继续获取下下位
            body = body.next
            # print(answer.val)
        # 通过 body 在 for 循环里的更新，后面每一位相连
        # 要返回的只是整个链表的第一位 ListNode 即最初定义的 answer
        # print(answer.val)
        return answer
Solution().addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4])