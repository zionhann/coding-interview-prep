base = input().upper()
number = int(base, 16)
for multiplier in range(1, 16):
    print(f"{base}*{multiplier:X}={number * multiplier:X}")
