def solution(my_string, queries):
    lst = list(my_string)
    
    for s, e in queries:
        lst[s:e+1] = lst[s:e+1][::-1]
        
    return "".join(lst)