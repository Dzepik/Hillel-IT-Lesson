"""
Минамальная и максимальная цена товара
"""

price = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003}

lower_limit = 35.9
upper_limit = 38.339

for price_item in price.items():
    if lower_limit <= price_item[1] <= upper_limit:
        print(price_item)