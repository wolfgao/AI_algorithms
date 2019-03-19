class ListNode:
    def __init__(self):
        self.val = None
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.node = None

    def add_node(self, data: ListNode):
        new_node = ListNode()
        new_node.val = data
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


if __name__ == '__main__':
    alinkedlist = SingleLinkedList()
    alinkedlist.add_node(1)
    alinkedlist.add_node(2)
    alinkedlist.add_node(4)
    alinkedlist.list_print()