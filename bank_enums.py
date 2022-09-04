from enum import Enum

class BankerOrClient(Enum):
    CLIENT = 1
    BANKER = 2

class ClientType(Enum):
    REGULAR = 1
    PREMIUM = 2
    VIP = 3

class BankActions(Enum):
    ADD_NEW_CLIENT = 1
    REMOVE_CLIENT = 2
    EXIT = 3

class UserActions(Enum):
    DEPOSIT = 1
    WITHDRAW = 2
    CHECK_BALANCE = 3
    EXIT = 4    

