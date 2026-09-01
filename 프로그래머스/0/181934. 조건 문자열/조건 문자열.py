def solution(ineq, eq, n, m):
    answer = 0
    
    if ineq == ">" and eq == "=":
        answer = n >= m
    elif ineq == "<" and eq == "=":
        answer = n <= m
    elif ineq == ">" and eq == "!":
        answer = n > m
    elif ineq == "<" and eq == "!":
        answer = n < m
        
    return 1 if answer else 0