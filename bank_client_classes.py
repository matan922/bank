class Client:
    cli_id = ""
    balance = 0
    allowed_minus = 0

    def __init__(self,cli_id="",balance=0, allowed_minus=0) -> None:
        self.cli_id = cli_id
        self.balance = balance
        self.allowed_minus = allowed_minus

    def withdraw(self):
        pass

    def deposit(self):
        pass

    def check_balance(self):
        return self.balance


class PremClient(Client):
    allowed_minus = -5000

class VipClient(Client):
    allowed_minus = -10000
