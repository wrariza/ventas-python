import sys

clients = 'pablo,ricardo,'


def print_not_client_list():
    print('Client not exist in the list clients')


def get_name_client(message='Name of client?'):
    name_client = None

    while not name_client:
        name_client = raw_input(message)

        if name_client == 'exit':
            name_client = None
            break

    if not name_client:
        sys.exit()

    return name_client


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


def _find_client(client_name):
    global clients

    clients = clients.split(',')

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


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
    print('[F] Find client')


if __name__ == "__main__":
    _print_welcom()
    command = raw_input().upper()

    if command == 'C':
        create_client(get_name_client())
    elif command == 'D':
        _delete_client(get_name_client())
    elif command == 'U':
        _update_client(get_name_client('Name client do you want update ?'), get_name_client())
    elif command == 'F':
        found =  _find_client(get_name_client('Name client do you want find ?'))
        if found:
            print('The client is in the list')
        else:
            print ('The client not is in the list')
    else:
        print('Invalid command')
