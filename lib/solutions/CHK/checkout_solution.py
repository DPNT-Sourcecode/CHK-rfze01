from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    products = sorted([i.strip(" ") for i in skus])
    products = Counter(products)
    cost = 0
    for sku, count in products.items:
        if i not in ["A", "B", "C", "D"]:
            return -1
        else:
            if
