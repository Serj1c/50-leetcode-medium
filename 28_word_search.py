def exist(board, word: str) -> bool:
    def traverse(board, i, j, word):
        if len(word) == 0:
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
            return False
            
        match = False
        original_letter = board[i][j]
        board[i][j] = '#'

        match = traverse(board, i + 1, j, word[1:]) or traverse(board, i - 1, j, word[1:]) or traverse(board, i, j + 1, word[1:]) or traverse(board, i, j - 1, word[1:])
        board[i][j] = original_letter
        return match

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and traverse(board, i, j, word):
                return True
        
    return False


print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))