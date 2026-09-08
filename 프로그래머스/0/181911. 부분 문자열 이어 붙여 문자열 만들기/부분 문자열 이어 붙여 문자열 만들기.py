def solution(my_strings, parts):
    answer = ''
    
    for word, (s, e) in zip(my_strings, parts):
        answer += word[s:e+1]
    
    return answer