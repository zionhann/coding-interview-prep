UNKNOWN = 0
RANK = [6, 6, 5, 4, 3, 2, 1]

def solution(lottos, win_nums):    
    match_count = 0
    zero_count = 0
    
    for number in lottos:
        if number == 0:
            zero_count += 1
            
        if number in win_nums:
            match_count += 1
    
    lowest = RANK[match_count]
    highest = RANK[match_count+zero_count]
    
    return [highest, lowest]