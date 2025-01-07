class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary_diag = 0
        secondary_diag = len(mat[0]) - 1
        final_sum = 0

        for row in mat:
            if primary_diag == secondary_diag:
                final_sum += row[primary_diag]
            else:
                final_sum += row[primary_diag] + row[secondary_diag]
            # print(row[primary_diag], row[secondary_diag])
            primary_diag += 1
            secondary_diag -= 1

        return final_sum