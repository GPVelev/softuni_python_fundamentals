orders = int(input())

total = 0
for _ in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsules < 1 or capsules > 2000:
        continue

    coffee_price = days * capsules * price_per_capsule
    total += coffee_price
    print(f'The price for the coffee is: ${coffee_price:.2f}')
print(f'Total: ${total:.2f}')

