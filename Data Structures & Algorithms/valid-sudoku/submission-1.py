class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row wise:- 
        for i in range(0, 9):
            lst = list()
            for j in range(0, 9):
                temp = board[i][j]
                if temp  != '.':
                    lst.append(temp)
            if len(set(lst)) != len(lst): 
                print('row')
                return False # Invalid 
        
        # column wise:- 
        for j in range(0, 9):
            lst = list()
            for i in range(0, 9):
                temp = board[i][j]
                if temp  != '.':
                    lst.append(temp)
            if len(set(lst)) != len(lst): 
                print('col')
                return False # Invalid 
        # 00, 03, 06: 30, 33, 36: 60, 63, 66 --> (0, 3, 6) (0, 3, 6)
        ## Block wise:- 
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                lst = list()
                # start:- (i, j) --> 3 right, 3 down 
                for k in range(0, 3):
                    temp1 = board[i+k][j+0]
                    temp2 = board[i+k][j+1]
                    temp3 = board[i+k][j+2]
                    
                    for temp in [temp1, temp2, temp3]:
                        if temp != '.': lst.append(temp)
                
                if len(set(lst)) != len(lst): 
                    print('box', len(lst), len(set(lst)), (i, j))
                    print(lst)
                    return False # Invalid 
        return True 