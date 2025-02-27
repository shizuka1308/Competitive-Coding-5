# The code finds the largest value in each level of a binary tree using BFS (level-order traversal). 
# It processes nodes level by level, keeping track of the maximum value in each level and appending it to the result list.

# Time Complexity: O(N) (Each node is visited once).
# Space Complexity: O(N) (In the worst case, the queue stores all nodes at the last level).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return []
        queue = deque([root])
        while queue:
            currMax = float('-inf')
            currLength = len(queue)
            for _ in range(currLength):
                node = queue.popleft()
                currMax = max(currMax, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(currMax)
        return ans