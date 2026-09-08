def solution(my_string, m, c):
    lst = [ my_string[i:i+m] for i in range(0, len(my_string), m)]
    return "".join((s[c-1] for s in lst))