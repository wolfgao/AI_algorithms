import math
from typing import List

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x: List):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def treeNode_list(self, root: List) -> List:
        '''

        :param root: List
        :return: List, the element is a TreeNode object
        '''
        #As a treenode, the array length must be beyond 2, at least 3.
        if len(root) <=2:
            return None

        tree_deep = 0
        width = 0
        current_pos = 0
        treeNodeList = []
        while tree_deep * width < len(root):
            width = int(math.pow(2, tree_deep))
            for j in range(width):
                node = TreeNode(root[current_pos])
                node.left = TreeNode(root[current_pos + width + j])
                node.right = TreeNode(root[current_pos + width + j + 1])
                treeNodeList.append(node)
                current_pos += 1
                print(node.val, node.left.val, node.right.val)
                if (current_pos + width + j + 1) >= len(root):
                    break
            tree_deep += 1
        return treeNodeList

    def lowestCommonAncestor(self, root, p, q):
        """
        https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/
        for example: root = [3,5,1,6,2,0,8,null,null,7,4]
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None
        if root is p or root is q:
            return root

        #dfs from the lest tree
        left = self.lowestCommonAncestor(TreeNode(root).left, p, q)
        #dfs from the right tree
        right = self.lowestCommonAncestor(TreeNode(root).right, p, q)

        if left is None and right is None:
            return None
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        else:
            return right

if __name__ == "__main__":
    root = [3,5,1,6,2,0,8,None,None,7,4]

    print(Solution().lowestCommonAncestor(root, 5, 1))
    print(Solution().lowestCommonAncestor(root, 5, 4))