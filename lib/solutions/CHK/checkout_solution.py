from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    combo_offer = ["X", "Z", "S", "T", "Y"]

    products = sorted([i.strip(" ") for i in skus])
    products = Counter(products)
    cost = 0
    for sku, count in products.items():
        if sku not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            return -1

    combo_count = products["X"] + products["T"] + products["S"] + products["Z"] + products["Y"]
    combo_packs = combo_count//

    count = products["E"]
    cost += count * 40
    if products['B'] > 0:
        products['B'] = max(0, products['B'] - (count // 2))

    count = products["N"]
    cost += count * 40
    if products['M'] > 0:
        products['M'] = max(0, products['M'] - (count // 3))

    count = products["R"]
    cost += count * 50
    if products['Q'] > 0:
        products['Q'] = max(0, products['Q'] - (count // 3))

    count = products["F"]
    cost += (count // 3) * 20
    cost += (count % 3) * 10

    count = products["U"]
    cost += (count // 4) * 120
    cost += (count % 4) * 40

    count = products["A"]
    cost += (count // 5) * 200
    newcount = count % 5
    cost += (newcount // 3) * 130
    cost += (newcount % 3) * 50

    count = products["H"]
    cost += (count // 10) * 80
    newcount = count % 10
    cost += (newcount // 5) * 45
    cost += (newcount % 5) * 10

    count = products["V"]
    cost += (count // 3) * 130
    newcount = count % 3
    cost += (newcount // 2) * 90
    cost += (newcount % 2) * 50

    count = products["B"]
    cost += (count // 2) * 45
    cost += (count % 2) * 30

    count = products["K"]
    cost += (count // 2) * 150
    cost += (count % 2) * 80

    count = products["P"]
    cost += (count // 5) * 200
    cost += (count % 5) * 50

    count = products["Q"]
    cost += (count // 3) * 80
    cost += (count % 3) * 30

    count = products["C"]
    cost += count * 20

    count = products["D"]
    cost += count * 15

    count = products["G"]
    cost += count * 20

    count = products["I"]
    cost += count * 35

    count = products["J"]
    cost += count * 60

    count = products["L"]
    cost += count * 90

    count = products["M"]
    cost += count * 15

    count = products["O"]
    cost += count * 10

    count = products["S"]
    cost += count * 30

    count = products["T"]
    cost += count * 20

    count = products["W"]
    cost += count * 20

    count = products["X"]
    cost += count * 90

    count = products["Y"]
    cost += count * 10

    count = products["Z"]
    cost += count * 50


    return cost





