"""
Two Sum: https://leetcode.com/problems/two-sum/

Input: nums = [2,7,11,15], target = 9, Output: [0,1]

Runtime: O(N)
"""

def two_sum(li, target): 
    dic = {} # value -> index
    for i in range(len(li)):
        if target - li[i] in dic:
            return [dic[target - li[i]], i]
        dic[li[i]] = i
        
if __name__ == "__main__":
    li = [2,7,11,15]
    target = 9
    output = two_sum(li, target)
    print(output == [0,1] or output == [1,0], output)
    