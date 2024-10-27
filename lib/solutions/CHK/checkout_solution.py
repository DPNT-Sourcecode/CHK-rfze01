from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    products = sorted([i.strip(" ") for i in skus])
    products = Counter(products)
    cost = 0
    for sku, count in products.items():
        if sku not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            return -1


    count = products["A"]
    cost += (count // 5) * 200
    newcount = count % 5
    cost += (newcount // 3) * 130
    cost += (newcount % 3) * 50

    count = products["E"]
    cost += count * 40
    if products['B'] > 0:
        products['B'] = max(0, products['B'] - (count//2))

    count = products["F"]
    cost += (count // 3) * 20
    cost += (count % 3) * 10

    count = products["B"]
    cost += (count // 2) * 45
    cost += (count % 2) * 30

    count = products["C"]
    cost += count * 20

    count = products["D"]
    cost += count * 15


    return cost

checkout('EEB')


