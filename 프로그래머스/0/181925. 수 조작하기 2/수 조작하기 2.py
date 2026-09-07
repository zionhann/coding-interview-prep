def solution(numLog):
    answer = ''
    
    for i, curr in enumerate(numLog[1:]):
        result = curr - numLog[i]
        
        if result == 1:
            answer += "w"
        elif result == -1:
            answer += "s"
        elif result == 10:
            answer += "d"
        elif result == -10:
            answer += "a"
            
    return answer