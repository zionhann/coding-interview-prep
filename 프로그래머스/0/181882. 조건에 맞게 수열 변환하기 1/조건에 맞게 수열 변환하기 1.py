def solution(arr):
    for i, e in enumerate(arr):
        if e >= 50 and e % 2 == 0:
            arr[i] //= 2
        elif e < 50 and e % 2 == 1:
            arr[i] *= 2
            
    return arr