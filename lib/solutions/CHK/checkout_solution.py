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
                cost += (count // 3) * 130
                cost += (count % 3) * 50
            elif sku == "B":
                cost += (count // 2) * 45
                cost += (count % 2) * 30
            elif sku == "C":
                

