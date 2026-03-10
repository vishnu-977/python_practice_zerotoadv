n = int(input())

store = {}
maxCost = 0
maxCostItem = ""

for i in range(n):
    item = input()
    quantity = int(input())
    price = int(input())

    totalPrice = quantity * price
    store[item] = store.get(item, 0) + totalPrice

total = 0

for key, val in store.items():
    if val > maxCost:
        maxCost = val
        maxCostItem = key
    total += val

average = total / n

print("Item: {} \nTotal price: {:.2f}\nAverage Price: {:.2f}".format(maxCostItem, total, average))