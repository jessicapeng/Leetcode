"""
Two Sum: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

It does not matter what you leave beyond the returned k (hence they are underscores).

Runtime: O(N), Space: O(1)
"""

def removeDuplicates(self, nums):
    # pt2 iterates to find unique one and pt1 is next index of the unique list you are building (insert index)
    pt1 = 1
    for i in range(1, len(nums)):
        pt2 = i
        if nums[i-1] != nums[i]:
            nums[pt1] = nums[i]
            pt1+=1
    return pt1 # size of unique elemnts is where first pointer ends
        
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    output = removeDuplicates(nums)
    print(output == 5 and nums[0:5] == [0,1,2,3,4])
    
