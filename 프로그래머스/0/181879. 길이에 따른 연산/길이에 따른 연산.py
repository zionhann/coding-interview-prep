import math 

def solution(num_list):
    size = len(num_list)
    
    if size > 10:
        return sum(num_list)
    else:
        return math.prod(num_list)
