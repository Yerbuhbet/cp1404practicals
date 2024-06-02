items = int(input("Number of items: "))
total_price = 0
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))

for _ in range(items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    total_price *= 0.9
print("Total price for", items, "items is", total_price)
