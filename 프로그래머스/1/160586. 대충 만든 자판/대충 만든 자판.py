def solution(keymap, targets):
    counter = [float('inf')] * 26
    answer = []
    
    for s in keymap:
        for i, c in enumerate(s):
            index = ord(c) - ord('A')
            
            if counter[index] > (i+1):
                counter[index] = (i+1) 
    
    for target in targets:
        total_count = 0
        
        for c in target:
            index = ord(c) - ord('A')
            
            if counter[index] == float('inf'):
                total_count = -1
                break
            
            total_count += counter[index]
        answer.append(total_count)
        total_count = 0
            
    return answer