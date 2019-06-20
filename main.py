clients = 'pablo,ricardo,'


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        list_clients()
    else:
        print('CLient already is in the client list')


def list_clients():
    print(clients)
    _add_comma


def _add_comma():
    global clients
    clients += ','


def _print_welcom():
    print('WELCOME TO VENTAS')
    print('*' * 55)
    print('what would you live to do today')
    print('[C] Create client')
    print('[D] Delete client')


if __name__ == "__main__":
    _print_welcom()
    command = raw_input()

    if command == 'C':
        name_client = raw_input('Name of client? ')
        create_client(name_client)

    elif command == 'D':
        pass
    else:
        print('Invalid command')
