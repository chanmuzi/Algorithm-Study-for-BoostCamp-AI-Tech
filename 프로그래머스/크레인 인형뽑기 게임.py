def solution(board, moves):
    n = len(board)
    basket = []
    cnt = 0
    for i in moves:
        for j in range(n):
            if board[j][i-1] != 0:
                temp = board[j][i-1]
                board[j][i-1] = 0

                if len(basket) != 0 and basket[-1] == temp:
                    basket.pop()
                    cnt += 2
                else:
                    basket.append(temp)
                break
            else: continue
    return cnt