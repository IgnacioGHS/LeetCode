# Taken from the user AlgoEngine. Here is his youtube video explaining the solution:
# https://www.youtube.com/watch?v=luicuNOBTAI

# This solution takes advantage of the fact that if x + y = target, then x = target - y. So, if you happen to 
# go through x and you've saved it, then you just have to take it out of the dictionary. This makes it so even 
# in the worst case, you go through nums only once, therefore, O(n).

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i