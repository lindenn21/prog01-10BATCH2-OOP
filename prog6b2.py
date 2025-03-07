first_input = int(input("Number 1:"))
for i in range(0, 9):
    num = int(input(f"Number {i + 2}:"))
    first_input -= num
print(first_input)


