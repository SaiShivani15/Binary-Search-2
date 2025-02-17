class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums==0 or len(nums)==None:
            return -1
        if nums==1:
            return 0
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=low+(high-low)//2
            if (mid==0 or nums[mid]>nums[mid-1])and (mid==len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            elif mid==0 or nums[mid]>nums[mid-1]:
                low=mid+1
            else:
                high=mid-1
        return -1
        