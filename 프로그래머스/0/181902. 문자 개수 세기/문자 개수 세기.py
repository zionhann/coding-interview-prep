def solution(my_string):
    result = [0] * 52
    targets = ["A", "B", "Z", "a", "b", "z"]
    
    for c in my_string:
        if 'A' <= c <='Z':
            result[ord(c) - ord('A')] += 1
        elif 'a' <= c <= 'z':
            result[ord(c) - ord('a') + 26] += 1
    
    return result
