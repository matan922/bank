from enum import Enum
from bank_class import Bank




class WorkerOrClient(Enum):
    CLIENT = 1
    WORKER = 2
    EXIT = 3

class ClientActions(Enum):
    DEPOSIT = 1
    WITHDRAW = 2
    BALANCE = 3

class WorkerActions(Enum):
    ADD_NEW_CLIENT = 1
    REMOVE_CLIENT = 2
    SEARCH_CLIENT = 3

class ClientType(Enum):
    REGULAR = 1
    PREMIUM = 2
    VIP = 3


def menu_client_worker():
    print(f"{WorkerOrClient.CLIENT.value} - {WorkerOrClient.CLIENT.name}")
    print(f"{WorkerOrClient.WORKER.value} - {WorkerOrClient.WORKER.name}")
    print(f"{WorkerOrClient.EXIT.value} - {WorkerOrClient.EXIT.name}")


def menu_client():
    print(f"{ClientActions.DEPOSIT.value} - {ClientActions.DEPOSIT.name}")
    print(f"{ClientActions.WITHDRAW.value} - {ClientActions.WITHDRAW.name}")
    print(f"{ClientActions.BALANCE.value} - {ClientActions.BALANCE.name}")
    selection = int(input("Choose what you want to do: "))
    if selection == ClientActions.DEPOSIT.value: return
    if selection == ClientActions.WITHDRAW.value: return
    if selection == ClientActions.BALANCE.value: return

    
def menu_worker():
    print(f"{WorkerActions.ADD_NEW_CLIENT.value} - {WorkerActions.ADD_NEW_CLIENT.name}")
    print(f"{WorkerActions.REMOVE_CLIENT.value} - {WorkerActions.REMOVE_CLIENT.name}")
    print(f"{WorkerActions.SEARCH_CLIENT.value} - {WorkerActions.SEARCH_CLIENT.name}")
    selection = int(input("Choose what you want to do: "))
    if selection == WorkerActions.ADD_NEW_CLIENT.value: Bank.add_new_reg_client()
    if selection == WorkerActions.REMOVE_CLIENT.value: return
    if selection == WorkerActions.SEARCH_CLIENT.value: return



def add_client_menu():
    print(f"{ClientType.REGULAR.value} - {ClientType.REGULAR.name}")
    print(f"{ClientType.PREMIUM.value} - {ClientType.PREMIUM.name}")
    print(f"{ClientType.VIP.value} - {ClientType.VIP.name}")
    selection = int(input("choose type of client: "))
    if selection == ClientType.REGULAR.value: Bank.add_new_reg_client(input("ID: "),input("Balance: "))
    if selection == ClientType.PREMIUM.value: Bank.add_new_prem_client()
    if selection == ClientType.VIP.value: Bank.add_new_vip_client()





def main():
    menu_client_worker()
    selection = int(input("Worker or client? "))
    while selection != WorkerOrClient.EXIT.value:
        if selection == WorkerOrClient.CLIENT.value:
            menu_client()
            return
        if selection == WorkerOrClient.WORKER.value:
            menu_worker()
            return
    
        







if __name__ == '__main__':
    main()