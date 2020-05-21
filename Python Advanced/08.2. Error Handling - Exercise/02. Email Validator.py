class MustContainAtSymbolError(Exception):
    def __init__(self):
        self.message = 'Email must contain @'
    def __str__(self):
        return self.message

class NameTooShortError(Exception):
    def __init__(self):
        self.message = 'Name must be more than 4 characters'
    def __str__(self):
        return self.message

class InvalidDomainError(Exception):
    def __init__(self):
        self.message = 'Domain must be one of the following: .com, .bg, .org,.net'
    def __str__(self):
        return self.message

command = input()
valid_domains = ['com', 'net', 'bg', 'org']

while command != 'End':
    email = command
    if '@' not in email:
        raise MustContainAtSymbolError
    if len(email.split('@')[0]) <= 4:
        raise NameTooShortError
    if not email.split('.')[-1] in valid_domains:
        raise InvalidDomainError
    print('Email is valid')
    command = input()