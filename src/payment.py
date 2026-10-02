def calculate_total(price, quantity, discount_percent=0):
    subtotal = price * quantity
    return subtotal - subtotal * discount_percent / 100
