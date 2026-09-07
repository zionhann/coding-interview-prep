from collections import Counter

def solution(a, b, c, d):
    counter = Counter([a, b, c, d])
    answer = 0
    
    if len(counter) == 1:
        return 1111 * a
    
    elif len(counter) == 2:
        items = counter.most_common()
        p, q = items[0][0], items[1][0]
        
        if items[0][1] == 3:
            return (10 * p + q) ** 2
        
        return (p + q) * abs(p - q)
        
    
    elif len(counter) == 3:
        q, r = [k for k, v in counter.items() if v == 1]
        return q * r
    else: 
        return min(counter.keys())
    
