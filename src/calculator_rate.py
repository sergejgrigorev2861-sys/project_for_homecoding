def calculate_discounted_price(price, rate):
    if price < 0:
        raise ValueError("Цена не может быть отрицательная")
    if rate < 0 or rate > 100:
        raise ValueError("Скидка должна быть от 0 до 100 процентов")
    return price - price * rate / 100