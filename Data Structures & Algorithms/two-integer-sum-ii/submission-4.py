class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        for i in range(len(numbers)):
            if (numbers[end] + numbers[start] > target):
                end -= 1
                continue
            if (numbers[end] + numbers[start] < target):
                start += 1
                continue
            return [start + 1, end + 1]
            
    
        