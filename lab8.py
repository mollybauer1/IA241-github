"""
lab 8
"""
#3.1
def wordCount(words):
    result = 0
    for word in words.split():
        result+=1
    return result

#3.2
demo_str = 'hello world!'
print(wordCount(demo_str))



#3.3
def findMin(nums):
    minNum = nums[0]
    for num in nums:
        if type(num) is not str:
            if num < minNum:
                minNum = num
    return minNum
    
#3.4
demo_list = [1,2,3,4,5,6] 
print(findMin(demo_list))

#3.5
mix_list = [1,2,3,4,'a',5,6]
print(findMin(mix_list))
