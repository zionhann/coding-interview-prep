def solution(arr):
    answer = 0
    prev = arr.copy()
    
    while True:
        for i, e in enumerate(arr):
            if e >= 50 and e % 2 == 0:
                arr[i] //= 2

            elif e < 50 and e % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        
        if prev == arr:
            return answer
        
        answer += 1
        prev = arr.copy()
    
    return answer