number = int(input())
if number < 0:
    print("A" if number % 2 == 0 else "B")
else:
    print("C" if number % 2 == 0 else "D")
