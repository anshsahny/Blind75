class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(value, adj, visited, stack):
            # Cycle detected
            if stack[value]:
                return True

            # Single Path Detected
            if value in visited:
                return False

            stack[value] = True
            visited.append(value)

            for child in adj[value]:
                if dfs(child, adj, visited, stack):
                    return True

            stack[value] = False
            
            return False

        adjacent = [[] for _ in range(numCourses)]
        # Stack to find cycle and visited to find single path
        stack, visited = [False] * numCourses, []

        for prerequisite in prerequisites:
            adjacent[prerequisite[1]].append(prerequisite[0])

        for i in range(numCourses):
            if dfs(i, adjacent, visited, stack):
                return False
        
        return True

        