from typing import List

class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.node = None

    def setList(self, nums: List):
        if nums:
            for data in nums:
                node = ListNode(data)
                self.add_node(node)

    def add_node(self, data: ListNode):
        new_node = data
        new_node.next = self.node
        self.node = new_node  #set the current node is the new node

    def list_print(self):
        node = self.node
        while node:
            print(node.val)
            node = node.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        https://leetcode.com/problems/reverse-linked-list/
        :param head: a single Linked list
        :return: A reverse Linked list
        '''
        current = head
        previous = None
        while (current != None):
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

    def detectCycle(self, head):
        """
        https://leetcode.com/problems/linked-list-cycle-ii/
        Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
        To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed)
        in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            print("no cycle")
            return None
        if head.next is None:
            print("no cycle")
            return None

        p_fast = p_slow = head

        while p_fast and p_slow and p_fast.next and p_slow.next:
            if p_fast.next is None: return None
            if p_fast.next.next is None: return None
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            if p_fast and p_slow and p_fast == p_slow:
                p_slow = head
                while p_slow != p_fast:
                    p_slow = p_slow.next
                    p_fast = p_fast.next
                return p_slow
        return None

    def addTwoNumbers(self, l1, l2):
        """
        https://leetcode.com/problems/add-two-numbers/
        You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order and each of their nodes contain a single digit.
        Add the two numbers and return it as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        Example:
            Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
            Output: 7 -> 0 -> 8
            Explanation: 342 + 465 = 807.
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = node = ListNode(0)
        carry = 0
        one_more_loop = False
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            node.next = ListNode(val)
            node = node.next
            if one_more_loop:
                break
            if l1 is None and l2 is None and carry>0:
                one_more_loop = True
        return root.next

if __name__ == '__main__':
    a = [5]
    b = [5]
    al = SingleLinkedList()
    al.setList(a)
    al.list_print()

    bl = SingleLinkedList()
    bl.setList(b)
    bl.list_print()

    cl = Solution().addTwoNumbers(al.node,bl.node)

    print(cl.val, cl.next.val)
