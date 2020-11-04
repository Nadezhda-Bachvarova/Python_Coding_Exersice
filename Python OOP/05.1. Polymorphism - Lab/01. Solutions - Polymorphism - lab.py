#TASK 1 - EXECUTE


def execute(func, *args):
    return func(*args)


#TEST CODE - 1:

def say_hello(name, my_name):
    print(f'Hello, {name}, I am {my_name}')


def say_bye(name):
    print(f'Bye, {name}')


execute(say_hello, 'Peter', 'George')
execute(say_bye, 'Peter')


#TASK 2 - INSTRUMENTALS


def play_instrument(instrument):
    return instrument.play()

#TEST CODE


class Guitar:

    def play(self):
        print('playing the guitar')


guitar = Guitar()
play_instrument(guitar)


class Piano:
    def play(self):
        print('playing the piano')


piano = Piano()
play_instrument(piano)


