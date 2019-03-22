class Solution(object):
    '''
    https://leetcode.com/problems/course-schedule/
    '''
    def canFinish_dfs(self, numCourses, prerequisites):
        """
        Reference:
        https://www.cnblogs.com/mcomco/p/10298021.html
        https://www.cnblogs.com/mcomco/p/10304383.html
        bfs and topical sort
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        marked = [0 for _ in range(numCourses)]

        for x,y in prerequisites:
            graph[x].append(y)

        ##dfs
        def dfs(i):
            if marked[i] == -1:
                return False
            if marked[i] == 1:
                return True
            marked[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            marked[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    def canFinish_bfs(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        # use the array to record each course entry degree
        degree = [0 for _ in range(numCourses)]


        for j, i in prerequisites:
            graph[i].append(j)
            degree[j] += 1
            #print(j, degree[j])
        # use the queue to record all courses can be read
        q = [i for i in range(numCourses) if degree[i] == 0]

        for i in q:
            for j in graph[i]:
                degree[j] -=1
                if degree[j] == 0:
                    q.append(j)
        #print(q)
        return len(q) ==numCourses


if __name__ == "__main__":
    graph1 = [[1,0]]
    graph2 = [[1,0],[0,1],[1,2]]
    #print(Solution().canFinish_dfs(2, graph1))
    #print(Solution().canFinish_dfs(3,graph2))
    print("bfs start....")
    print(Solution().canFinish_bfs(2, graph1))
    print(Solution().canFinish_bfs(3, graph2))