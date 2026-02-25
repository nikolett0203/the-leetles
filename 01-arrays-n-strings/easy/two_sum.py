

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # declare a hashmap
        h = {}

        # store numbers as hashes and indices as values
        for i, num in enumerate(nums):
            h[num] = i

        for i, num in enumerate(nums):
            # figure out what value we need to sum up to the target
            need = target - num 

            # if that humber exists in the hashmap, and is a different element...
            if need in h and h[need] != i:
                #...return our two indices
                return i, h[need]
