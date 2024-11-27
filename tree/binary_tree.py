from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while i < len(values):
        current = queue.pop(0)

        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1 = []
        list2 = []
        stack1 = []
        stack2 = []
        stack1.append(root1)
        while len(stack1):
            pre1 = stack1.pop()
            if pre1.right:
                stack1.append(pre1.right)
            if pre1.left:
                stack1.append(pre1.left)
            if pre1.left is None and pre1.right is None:
                list1.append(pre1.val)
        stack2.append(root2)
        while len(stack2):
            pre2 = stack2.pop()
            if pre2.right:
                stack2.append(pre2.right)
            if pre2.left:
                stack2.append(pre2.left)
            if pre2.left is None and pre2.right is None:
                list2.append(pre2.val)
        print(list1)
        print(list2)
        if list1==list2:
            return True
        else:
            return False



# list1 = [3,5,1,6,2,9,8,None,None,7,4]
# list2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
# tree1 = build_tree_from_list(list1)
# tree2 = build_tree_from_list(list2)
s = Solution()
# s.leafSimilar(tree1,tree2)
c = [4,3,6,1,None,5,None,None,2]
tree = build_tree_from_list(c)