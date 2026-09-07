def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        result = min([arr[i] for i in range(s, e+1) if arr[i] > k], default=-1)
        answer.append(result)
        
    return answer