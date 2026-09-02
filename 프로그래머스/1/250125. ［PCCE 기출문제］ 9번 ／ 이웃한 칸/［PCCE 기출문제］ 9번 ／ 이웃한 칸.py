def solution(board, h, w):
    answer = 0
    n = len(board)
    
    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    
    for i in range(4):
        h_next = h + dh[i]
        w_next = w + dw[i]
        
        if 0 <= h_next < n and 0 <= w_next < n:
            if board[h][w] == board[h_next][w_next]: 
                answer += 1
    return answer