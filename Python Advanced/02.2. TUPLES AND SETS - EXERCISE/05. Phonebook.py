phonebook = {}
command = input()

while command != 'search':
    tokens = command.split('-')
    name = tokens[0]
    number = tokens[1]
    phonebook[name] = number #creat and save new number in dictonary

    command = input()

command = input()

while command != 'stop':
    name = command
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')

    command = input()