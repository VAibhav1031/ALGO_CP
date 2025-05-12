def ways_to_put_n_queens(n: int) -> int:

    def solve(board,row):
        if row == n:
            display(board)
            print()
            return 1 
        
        count = 0
        for col in range(n):
            if  safe(row,col,board):
                board[row][col] = False 
                count += solve(board,row+1)
                board[row][col] = True

        return count



    def safe(row,col, board):
        # we have to check the  all the vertical rows  and  columns, diagonal and anti diagonal
        
        ## vertically means we have  to go in the column 
        for r in range(n):
            if board[r][col] == False:
                return False

        for c in range(n):
            if board[row][c] == False:
                return False

        # diagonal
        # biggest question , 
        for d1 in range(n):
            if 0<= row-d1 <n  and 0<= col -d1 <n  and  board[row-d1][col-d1] == False:
                return False


            if 0<= row+d1 <n  and 0<= col+d1 <n  and  board[row+d1][col+d1] == False:
                return False

        # Anti-diagonal
        for d2 in range(n):
            if 0<= row-d2 <n  and 0<= col+d2 <n  and  board[row-d2][col+d2] == False:
                return False


            if 0<= row+d2 <n  and 0<= col-d2 <n  and  board[row+d2][col-d2] == False:
                return False



        return True



    def display(board):
        for r in range(n):
            for c in range(n):
                if board[r][c] == False:
                    print("Q",end = " ")

                else:
                    print("x", end = " ")

            print()


    board = [[True]*n for _ in range(n)]
    return solve(board,0)


if __name__ == "__main__":
    n = int(input("Enter the n :"))
    print(ways_to_put_n_queens(n))
        


