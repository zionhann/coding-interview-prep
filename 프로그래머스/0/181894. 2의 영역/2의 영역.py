def solution(arr):
    if 2 not in arr:
        return [-1]
    
    indices = [i for i, v in enumerate(arr) if v == 2]
    
    return arr[indices[0]:indices[-1]+1]