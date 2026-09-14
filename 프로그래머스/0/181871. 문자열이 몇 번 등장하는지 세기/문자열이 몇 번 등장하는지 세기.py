def solution(myString, pat):
    window = len(pat)
    size = len(myString) - window
    answer = 0
    
    for i in range(size+1):
        s = myString[i:i+window]
        
        if s == pat:
            answer += 1
        
    return answer