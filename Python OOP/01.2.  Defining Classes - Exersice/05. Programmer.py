class Programmer:
    result = ''

    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language in self.language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {language}'

    def change_language(self, new_language, skills_needed):
        if new_language in self.language:
            return f'{self.name} already knows {new_language}'
        elif self.skills >= skills_needed:
            result = f'{self.name} switched from {self.language} to {new_language}'
            self.language = new_language
            return result
        return f'{self.name} needs {skills_needed - self.skills} more skills'


# Test code:

programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))

# Expected output:

# John does not know Python
# John already knows Java
# John needs 50 more skills
# John watched Java: zero to hero
# John switched from Java to Python
# John watched Python Masterclass

