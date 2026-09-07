count = [0] * 24
input()
for number in map(int, input().split()):
    count[number] += 1
print(*count[1:])
