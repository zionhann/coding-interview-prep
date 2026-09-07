h, b, c, s = map(int, input().split())
megabytes = h * b * c * s / 8 / 1024 / 1024
print(f"{megabytes:.1f} MB")
