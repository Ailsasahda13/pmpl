
class PaymentResult:
    def __init__(self, success):
        self.success = success


class Wallet:
    def __init__(self, balance, provider):
        self.balance = balance
        self.provider = provider

    def pay(self, amount):
        response = self.provider.charge(amount)

        if response["status"] == "ACCEPTED":
            if self.balance >= amount:
                self.balance -= amount
                return PaymentResult(success=True)

        return PaymentResult(success=False)
