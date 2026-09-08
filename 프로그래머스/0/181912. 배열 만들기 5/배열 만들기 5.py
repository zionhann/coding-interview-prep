def solution(intStrs, k, s, l):
    answer = []
    
    for intstr in intStrs:
        
        if (sliced := int(intstr[s:s+l])) > k:
            answer.append(sliced)
            
    return answer