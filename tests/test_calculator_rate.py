import pytest
from src.calculator_rate import calculate_discounted_price

@pytest.mark.parametrize("price, rate, expected", [
    (1000, 0, 1000),    # скидка 0%
    (1000, 50, 500),    # скидка 50%
    (1000, 100, 0),      # скидка 100%
    (99.99, 10, 89.991) # цена с копейками
])
def test_calculate_discounted_price(price, rate, expected):
    assert calculate_discounted_price(price, rate) == expected

@pytest.mark.parametrize("price, rate, error_msg", [
    (-100, 10, "Цена не может быть отрицательная"),
    (100, -5, "Скидка должна быть от 0 до 100 процентов"),
    (100, 150, "Скидка должна быть от 0 до 100 процентов"),
])
def test_discount_errors(price, rate, error_msg):
    with pytest.raises(ValueError, match=error_msg):
        calculate_discounted_price(price, rate)
