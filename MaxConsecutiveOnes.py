class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        savedCount = 0
        for num in nums:
            if(num == 1) : 
                count = count + 1
                savedCount = max(savedCount, count)
                # print("counting",nums[i],count)
            else       :
                # print("else case",nums[i])
                
                
                count = 0

        print ("output",savedCount)         


mySolution = Solution()
mySolution.findMaxConsecutiveOnes([1,1,0,1,1,1])