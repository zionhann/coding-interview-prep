number = int(input())
for value in range(1, number + 1):
    print("X" if any(digit in "369" for digit in str(value)) else value, end=" ")
