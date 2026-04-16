class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(len(board))]

        # Traverse through each row
        for i in range(len(board)):
            # Traverse through each column
            for j in range(len(board)):
                num = board[i][j]

                # Check if num is a number or a "."
                if num == ".":
                    continue

                # Check if number already appears in the row.
                # If not, add it to the set for the row.
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # Check if number already appears in the column.
                # If not, add it to the set for the column.
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # Calculate which 3x3 box the number appears in
                b_row = (i // 3) * 3
                b_col = (j // 3)
                b_i = b_row + b_col

                # Check if number already appears in the column.
                # If not, add it to the set for the column.
                if num in boxes[b_i]:
                    return False
                boxes[b_i].add(num)

        return True




