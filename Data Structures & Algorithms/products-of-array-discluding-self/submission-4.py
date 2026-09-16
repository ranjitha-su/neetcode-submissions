class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_product=[1]*n
        right_product=[1]*n
        output=[1]*n
        for i in range(len(nums)):
            if i==0:
                continue
            if i==1:
                left_product[i]=nums[i-1]
            left_product[i]=nums[i-1]*left_product[i-1]
        for i in reversed(range(n)):
            if i==n-1:
                continue
            if i==n-2:
                right_product[i]=nums[i+1]
            right_product[i]=right_product[i+1]*nums[i+1]

        for index in range(n):
            output[index]=left_product[index]*right_product[index]
        return output
