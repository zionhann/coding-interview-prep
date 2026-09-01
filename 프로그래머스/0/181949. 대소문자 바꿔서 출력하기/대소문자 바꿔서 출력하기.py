str = input()

for c in str:
    print(chr(ord(c)^32), end="")