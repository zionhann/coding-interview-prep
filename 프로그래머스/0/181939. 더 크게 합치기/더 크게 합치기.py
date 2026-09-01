def solution(a, b):
    n1 = int("".join([str(a), str(b)]))
    n2 = int("".join([str(b), str(a)]))
    
    return n1 if n1 >= n2 else n2