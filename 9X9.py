def get_products(a=1, b=9, c=1, d=9):
    return [x * y for x in range(a, b+1) for y in range(c, d+1)]