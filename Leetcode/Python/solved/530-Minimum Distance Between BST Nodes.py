#530 Minimum Distance Between BST Nodes
'''
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
 

Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        vals = []
        def aux(root:TreeNode):
            if not root:return
            aux(root.left)
            vals.append(root.val)   
            aux(root.right)
        aux(root)
        minimumDifference = float("inf")
        for i in range(1,len(vals)):
            minimumDifference = min(minimumDifference, vals[i] - vals[i-1])
        return minimumDifference