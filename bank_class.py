from bank_client_classes import Client


class Bank:
    reg_clients = []
    prem_clients = []
    vip_clients = []


    def __init__(self) -> None:
        pass


    def add_new_reg_client(self,cli_id="",balance=0):
        self.reg_clients.append(Client(cli_id,balance))

    def add_new_prem_client(self,cli_id="",balance=0):
        self.prem_clients.append(Client(cli_id,balance))

    def add_new_vip_client(self,cli_id="",balance=0):
        self.vip_clients.append(Client(cli_id,balance))

    def remove_client(self,cli_id="",balance=0):
        self.reg_clients.remove(Client(cli_id,balance))

    def search_client(self,cli_id="",balance=0):
        for client in self.reg_clients:
            print(client.cli_id)
            
            

    def print_clients(self):
        for client in self.reg_clients:
            print(f"ID: {client.cli_id} , Balance: {client.balance}")

            

    



