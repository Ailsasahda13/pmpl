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

    # --- LAB 2 TESTS ---
    # Row 1: Testing exact value (Rp67,500)
    def test_order_total_value():
        total = order_total(22500, 3)
        assert total == 67500


    # Row 2: Testing error message containing "qty"
    def test_zero_qty_error_message():
        with pytest.raises(ValueError) as err:
            order_total(25000, 0)
        assert "qty" in str(err.value)


    # Row 3: Testing count of notifications (empty)
    def test_no_notifications():
        notifications = [] 
        assert len(notifications) == 0
