from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    products = sorted([i.strip(" ") for i in skus])
    products = Counter(products)
    cost = 0
    for sku, count in products.items():
        if sku not in ["A", "B", "C", "D"]:
            return -1
        else:
            if sku == "A":
                cost += (count // 5) * 200
                newcount = count % 5
                cost += (newcount // 3) * 130
                cost += (newcount % 3) * 40
            elif sku == "B":
                cost += (count // 2) * 45
                cost += (count % 2) * 30
            elif sku == "C":
                cost += count * 20
            elif sku == "D":
                cost += count * 15
            elif sku == "E":
                cost += count * 40
    return cost


