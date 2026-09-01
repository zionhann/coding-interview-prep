def solution(a, b):
    expr1 = int("".join([str(a), str(b)]))
    expr2 = 2 * a * b
    return expr1 if expr1 >= expr2 else expr2