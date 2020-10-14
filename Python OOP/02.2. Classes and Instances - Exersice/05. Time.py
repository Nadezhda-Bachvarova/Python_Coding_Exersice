class Time:
    max_hours = 24
    max_minutes = 60
    max_seconds = 60

    def __init__(self, hours, minutes, seconds):
        self.seconds = seconds
        self.hours = hours
        self.minutes = minutes

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        self.seconds += 1
        if self.seconds >= Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours >= Time.max_hours:
                    self.hours = 0
        return self.get_time()


# Test Code 1:

time = Time(9, 30, 60)
print(time.next_second())

# Expected Output 1:

# 09:31:00

# ---------------------------

# Test Code 2:

time = Time(10, 59, 59)
print(time.next_second())

# Expected Output 2:

# 11:00:00

# ---------------------------

# Test Code 3:

time = Time(24, 59, 59)
print(time.next_second())

# Expected Output 3:

# 01:00:00
