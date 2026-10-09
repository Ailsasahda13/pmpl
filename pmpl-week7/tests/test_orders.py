import pytest
from campusgo.order import order_total, Order

# --- LAB 1 TEST ---
def test_order_total_with_promo():
    price = 25000
    qty = 2
    has_promo = True
    total = order_total(price, qty, has_promo)
    assert total == 45000

# --- LAB 2 TESTS ---
def test_order_total_value():
    total = order_total(22500, 3)
    assert total == 67500

def test_no_notifications():
    notifications = []
    assert len(notifications) == 0

# --- LAB 3 ---
def test_zero_qty_is_rejected():
    with pytest.raises(ValueError) as err:
        order_total(25000, 0)
    assert "qty" in str(err.value) 

def test_negative_qty_is_rejected():
    with pytest.raises(ValueError) as err:
        order_total(25000, -1)
    assert "qty" in str(err.value) 

# --- LAB 4: FIXTURES AS PRECONDITIONS ---

@pytest.fixture
def processing_order():
    order = Order(id="ORD-T003", owner="U-01", total=25000)
    order.status = "PROCESSING"
    yield order
    order.status = "UNPAID"
    order.tenant_notifications.clear()


def test_processing_order_cannot_be_cancelled(processing_order):
    result = processing_order.cancel(by="U-01")

    assert result.rejected is True
    assert result.message == "Order is being processed"
    assert processing_order.status == "PROCESSING"
    assert processing_order.tenant_notifications == []