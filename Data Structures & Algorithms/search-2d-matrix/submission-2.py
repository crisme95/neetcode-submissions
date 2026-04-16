class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        lr, rr = 0, len(matrix) - 1
        row = -1

        while lr <= rr:
            mr = lr + ((rr - lr) // 2)

            # If target is less than first element in row, it can't be in there
            if matrix[mr][0] > target:
                rr = mr - 1
            # If the target is the beginning or end of the row, return True
            elif matrix[mr][0] == target or matrix[mr][-1] == target:
                return True
            # If the target is within the range of the row, return row number
            elif matrix[mr][0] < target and matrix[mr][-1] > target:
                row = mr
                break
            # The target is greater than the last element in the row, so don't check earlier ones
            else:
                lr = mr + 1

        if row == -1:
            return False
        # Now do binary search on the row
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        
        return False