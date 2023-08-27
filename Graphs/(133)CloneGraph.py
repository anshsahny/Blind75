"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue, copiedNodes = [], {node.val: Node(node.val, [])}

        queue.append(node)
        
        while queue:
            curr = queue[0]

            for child in curr.neighbors:
                if child.val not in copiedNodes:
                    copiedNodes[child.val] = Node(child.val, [])
                    queue.append(child)

                copiedNodes[curr.val].neighbors.append(copiedNodes[child.val])

            queue.pop(0)

        return copiedNodes[node.val]