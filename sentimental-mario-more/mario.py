from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

for i in range(height):
    print(" " * int(height-(i+1)), end="")
    print("#" * int(i+1), end="  ")
    print("#" * int(i+1))
