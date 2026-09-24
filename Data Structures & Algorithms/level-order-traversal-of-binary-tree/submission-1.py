# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def get_neighbors(node: Optional[TreeNode]):
            neighbors=[]
            if node.left:
                neighbors.append(node.left)
            if node.right:
                neighbors.append(node.right)
            # print(f"cur_node: {node}, neighbors: [{node.left, node.right}]")
            return neighbors

        q=deque()
        if root:
            q.append(root)
        output=[]
        while q:
            level_size=len(q)
            cur_level_nodes=[]
            for _ in range(level_size):
                cur_node=q.popleft()
                cur_level_nodes.append(cur_node.val)
                for neighbor in get_neighbors(cur_node):
                    q.append(neighbor)
            output.append(cur_level_nodes)
        return output