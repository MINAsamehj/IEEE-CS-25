lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

n = int(input())

if all(digit in '47' for digit in str(n)):
    print("YES")
elif any(n % lucky == 0 for lucky in lucky_numbers):
    print("YES")
else:
    print("NO")
