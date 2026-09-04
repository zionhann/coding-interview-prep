def solution(code):
    answer = ''
    mode = 0
    
    for i, c in enumerate(code):
        if c == "1":
            mode = not mode
            continue
        
        if mode == 0 and i % 2 == 0:
            answer += c
        
        elif mode == 1 and i % 2 == 1:
            answer += c

    if not answer:
        return "EMPTY"

    return answer