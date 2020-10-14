class Smartphone:

    def __init__(self, memory):
        self.memory = memory
        self.memory_taken = 0
        self.apps = []
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if not self.is_on:
            return f'Turn on your phone to install {app}'

        memory_left = self.memory - self.memory_taken
        if memory_left < app_memory:
            return f'Not enough memory to install {app}'

        self.memory_taken += app_memory
        self.apps.append(app)
        return f'Installing {app}'

    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.memory - self.memory_taken
        return f'Total apps: {total_apps_count}. Memory left: {memory_left}'


# Test code:

smartphone = Smartphone(100)
print(smartphone.install('Facebook', 60))
smartphone.power()
print(smartphone.install('Facebook', 60))
print(smartphone.install('Messenger', 20))
print(smartphone.install('Instagram', 40))
print(smartphone.status())


# Expected output:

# Turn on your phone to install Facebook
# Installing Facebook
# Installing Messenger
# Not enough memory to install Instagram
# Total apps: 2. Memory left: 20