n = int(input())

ascii_sum = 0
for _ in range(n):
    letter = ord(input())
    ascii_sum += letter
print(f'The sum equals: {ascii_sum}')