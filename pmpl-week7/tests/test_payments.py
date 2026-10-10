from unittest.mock import Mock
from campusgo.wallet import Wallet


def test_failed_payment_leaves_balance_unchanged():
    provider = Mock()
    provider.charge.return_value = {"status": "REJECTED"}

    wallet = Wallet(balance=24000, provider=provider)

    result = wallet.pay(25000)

    assert result.success is False
    assert wallet.balance == 24000
    provider.charge.assert_called_once_with(25000)

def test_accepted_payment_reduces_balance_to_zero():
    provider = Mock()
    provider.charge.return_value = {"status": "ACCEPTED"}

    wallet = Wallet(balance=25000, provider=provider)
    result = wallet.pay(25000)

    assert result.success is True
    assert wallet.balance == 0
    provider.charge.assert_called_once_with(25000)
