from typing import List

class Solution:
    '''
    https://leetcode.com/problems/two-sum/
    https://leetcode.com/problems/product-of-array-except-self/
    https://leetcode.com/problems/minimum-path-sum/
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Try to get the kth largest number of this array, supposed all are int numbers.
        :param nums: a not empty array
        :param k: the kth
        :return: num: the kth largest number in this array
        '''
        if len(nums) <=0: return None
        nums.sort(reverse=True)
        return nums[k-1]

    def findMin(self, nums: List[int]) -> int:
        '''
        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
        (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]). Find the minimum element.
        You may assume no duplicate exists in the array.
        :param nums: the initial array
        :return: int: the minimum number
        '''
        if len(nums) < 1: return None
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return min(nums)
        min_num = nums[0]
        for i in range(len(nums)):
            if min_num > nums[i]:
                min_num = nums[i]
        return min_num

    def minPathSum(self, grid):
        """
        这应该是一个动态规划的算法，复杂度是O(m*n),因为每一个元素都要遍历一遍
        解体思路：
        假设从起点走到第i行第j列的最小路径和为dp[i][j]，第i行第j列的格子上的值为grid[i][j]
        那么dp[i][j]=min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        即dp[i][j]为这个格子的左边和上面两个格子的路径和中最小的那个值加上这个格子本身的值的和。
        通过遍历数组就可以得到每一个dp[i][j]，而最后的dp[m-1][n-1]就是到达右下角的最小路径和。
        :type grid: List[List[int]]，这是一个二维数组
        :rtype: int，返回最小路径
        """
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0: return None
        if m == 1 and n == 1: return grid[m - 1][n - 1]

        # didn't change the original grid
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(m):
            for j in range(n):
                # 第一个元素
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                # 最上面的一排元素
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                # 最左边的一列元素，只能往下走
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return min(dp[m - 1][n - 2], dp[m - 2][n - 1]) + grid[m - 1][n - 1]

if __name__ == '__main__' :
    a1 = [3,2,1,5,6,4]
    a2 = [3,2,3,1,2,4,5,5,6]
    #print(Solution().findKthLargest(a2,3))
    a3 =[4,5,6,7,0,1,2]
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    grid2 =[[2]]
    #print(Solution().findMin(a3))
    print(Solution().minPathSum(grid))
