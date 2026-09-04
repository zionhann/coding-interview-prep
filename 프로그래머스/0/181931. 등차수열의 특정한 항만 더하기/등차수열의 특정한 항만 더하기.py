def solution(a, d, included):
    answer = 0
    arr = [a]
    
    for i in range(len(included)-1):
        arr.append(arr[-1] + d)
        
    for i, is_true in enumerate(included):
        if is_true: answer += arr[i]

    return answer