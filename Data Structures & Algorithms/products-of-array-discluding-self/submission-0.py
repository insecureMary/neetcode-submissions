class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newList = []
        for i, value in enumerate(nums):
           tempList = nums[:]
           tempList[i] = tempList[-1]
           tempList.pop()
           newProd = math.prod(tempList)
           newList.append(newProd)
        return newList

             
        