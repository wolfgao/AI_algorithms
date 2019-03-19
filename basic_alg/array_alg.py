from typing import List

class Solution:
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

if __name__ == '__main__':
    a1 = [3,2,1,5,6,4]
    a2 = [3,2,3,1,2,4,5,5,6]
    #print(Solution().findKthLargest(a2,3))
    a3 =[4,5,6,7,0,1,2]
    print(Solution().findMin(a3))