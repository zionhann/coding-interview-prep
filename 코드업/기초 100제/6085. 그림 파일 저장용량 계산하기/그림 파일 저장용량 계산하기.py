w, h, b = map(int, input().split())
megabytes = w * h * b / 8 / 1024 / 1024
print(f"{megabytes:.2f} MB")
