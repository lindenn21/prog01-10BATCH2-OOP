EVEN = 0
for i in range(0, 10):
    num = float(input(f"Number {i + 1}: "))
    if num % 2 == 0:
        EVEN += 1
print(EVEN)
