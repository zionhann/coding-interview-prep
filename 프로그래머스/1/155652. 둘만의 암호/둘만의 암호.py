"""
1. n만큼 뒤에 있는 알파벳 찾기 (z 넘어가면 a로 오는것도)
2. skip 고려한 알파벳 찾기

"""

def solution(s, skip, index):
    answer = ''
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
          'h', 'i', 'j', 'k', 'l', 'm', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    
    letters = [c for c in alphabets if c not in skip]
    l = len(letters)
    
    for c in s:
        begin = letters.index(c)
        decrypted = letters[(begin+index) % l]
        answer += decrypted
    return answer