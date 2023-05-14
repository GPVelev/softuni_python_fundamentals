n = int(input())
numbers = []
filtered = []

for i in range(n):
    current_number = int(input())
    numbers.append(current_number)

commmand = input()
if commmand == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
elif commmand == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
elif commmand == "negative":
    for number in numbers:
        if number < 0:
            filtered.append(number)
elif commmand == "positive":
    for number in numbers:
        if number >= 0:
            filtered.append(number)
print(filtered)
