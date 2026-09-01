def solution(n):
    answer_odd = 0
    answer_even = 0
    
    for i in range(1, n+1):
        if i % 2 == 0:
            answer_even += i**2
            continue
        answer_odd += i

    return answer_even if n % 2 == 0 else answer_odd