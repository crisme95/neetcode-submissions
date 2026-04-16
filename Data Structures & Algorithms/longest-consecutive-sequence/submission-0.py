class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest_seq = 0

        for num in nums:
            if (num - 1) not in nums_set:
                seq_len = 1
                curr_num = num
                while (curr_num + 1) in nums_set:
                    curr_num += 1
                    seq_len += 1

                if longest_seq < seq_len:
                    longest_seq = seq_len
        
        return longest_seq


