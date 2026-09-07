def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        s = str(i)
        
        if all(c in "05" for c in s):
            answer.append(i)
        
    return answer if answer else [-1]