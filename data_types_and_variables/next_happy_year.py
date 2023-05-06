year = int(input())

year_as_str = str(year)
year += 1

while len(year_as_str) != len(set(year_as_str)):
    year += 1
    year_as_str = str(year)

print(f'{year}')
