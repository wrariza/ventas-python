clients = 'pablo,ricardo,'


def print_not_client_list():
    print('Client not exist in the list clients')


def get_name_client(message='Name of client?'):
    return raw_input(message)


def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        list_clients()
    else:
        print('client exist in the list')


def _update_client(client_name, new_value_client):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name, new_value_client)
        list_clients()
    else:
        print_not_client_list()


def _delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name+',', '')
        list_clients()
    else:
        print_not_client_list()


def list_clients():
    print(clients)
    _add_comma()


def _add_comma():
    global clients
    clients += ','


def _print_welcom():
    print('WELCOME TO VENTAS')
    print('*' * 55)
    print('what would you live to do today')
    print('[C] Create client')
    print('[D] Delete client')
    print('[U] Update client')


if __name__ == "__main__":
    _print_welcom()
    command = raw_input().upper()

    if command == 'C':
        create_client(get_name_client())
    elif command == 'D':
        _delete_client(get_name_client())
    elif command == 'U':
        _update_client(get_name_client('Name client do you want update ?'), get_name_client())
    else:
        print('Invalid command')
