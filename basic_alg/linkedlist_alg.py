class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
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

