def calculate_total(price, quantity, discount_percent=0):
    subtotal = price * quantity
    # BUG: diskon ditambahkan, seharusnya dikurangi
    return subtotal + subtotal * discount_percent / 100
