capacity = 255

lines = int(input())
tank = 0
for water in range(lines):
    liters = int(input())
    tank += liters
    if tank > capacity:
        print("Insufficient capacity!")
        tank -= liters
        continue


print(tank)