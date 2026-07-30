class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_hash = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        row_hash = {}
        column_hash = {}

        for row_i, row in enumerate(board):
            row_hash[row_i] = row
            for col_i, number in enumerate(row):
                column_hash[col_i] = column_hash.get(col_i, []) + [number]

                box_i = (row_i // 3) * 3 + (col_i // 3)
                box_hash[box_i].append(number)
    

        for row_list in row_hash.values():
            for i in range(len(row_list)):
                            for j in range(len(row_list)):
                                if row_list[i] == row_list[j] and i != j and row_list[i] != "." and row_list[j] != ".":
                                    return False

        for column_list in column_hash.values():
                    for i in range(len(column_list)):
                                    for j in range(len(column_list)):
                                        if column_list[i] == column_list[j] and i != j and column_list[i] != "." and column_list[j] != ".":
                                            return False
            
        for box_list in box_hash.values():
                            for i in range(len(box_list)):
                                            for j in range(len(box_list)):
                                                if box_list[i] == box_list[j] and i != j and box_list[i] != "." and box_list[j] != ".":
                                                    return False

        return True


        
        

