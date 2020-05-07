def read_until_command(end_command):
    commands_list = []
    while True:
        command = input()
        if end_command == command:
            return commands_list
        commands_list.append(command)


def solve(commands_list):
    parking_lot = set()
    cars = []
    for command_string in commands_list:
        (command, car_number) = command_string.split(', ')
        cars.append(car_number)
        if command == 'IN':
            parking_lot.add(car_number)
        else:
            parking_lot.remove(car_number)
    cars = cars[::-1]
    result = sorted(parking_lot, key=lambda x: -cars.index(x))
    if result:
        [print(x) for x in result]
    else:
        print('Parking Lot is Empty')


commands_list = read_until_command('END')
solve(commands_list)