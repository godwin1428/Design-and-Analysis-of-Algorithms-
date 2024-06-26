def game_of_life(board):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    m, n = len(board), len(board[0])
    def count_live_neighbors(x, y):
        count = 0
        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]
            if 0 <= nx < m and 0 <= ny < n and abs(board[nx][ny]) == 1:
                count += 1
        return count
    for i in range(m):
        for j in range(n):
            live_neighbors = count_live_neighbors(i, j)
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = 2  
            if board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = -1  
    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0  
            if board[i][j] == -1:
                board[i][j] = 1  
    return board
board1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
print(game_of_life(board1))
board2 = [[1, 1], [1, 0]]
print(game_of_life(board2))
