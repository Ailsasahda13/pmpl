import pytest
from campusgo.order import order_total

def test_order_total_with_promo():
    # Arrange
    price = 25000
    qty = 2
    has_promo = True

    # Act
    total = order_total(price, qty, has_promo)

    # Assert
    assert total == 45000

    
