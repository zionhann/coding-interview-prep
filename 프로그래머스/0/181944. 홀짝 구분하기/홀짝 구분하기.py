a = int(input())

print(f"{a} is ", end="")
print("even") if a % 2 == 0 else print("odd")