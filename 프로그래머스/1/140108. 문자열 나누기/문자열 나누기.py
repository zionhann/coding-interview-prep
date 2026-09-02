def solution(s):
    x = s[0]
    l = len(s)
    
    c1 = c2 = answer = 0
    word = ''
    
    for i in range(l):
        if s[i] == x: c1 += 1
        else: c2 += 1

        word += s[i]
        
        if c1 == c2:
            answer += 1
            word = ''
            c1 = c2 = 0
            
            if i+1 < l:
                x = s[i+1]
    
    if c1 != c2:
        answer += 1
    return answer