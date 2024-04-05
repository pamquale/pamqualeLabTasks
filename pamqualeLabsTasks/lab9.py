import re


class Lab9:
    def __init__(self, s):
        self.s = s

    def task1(self):
        return bool(re.match(r'^[a-z0-9]+$', self.s))

    def task2(self):
        return bool(re.search(r'[A-Z]', self.s))

    def task3(self):
        return bool(re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', self.s))

    def task4(self):
        return bool(re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$', self.s))

    def task5(self):
        return bool(re.match(r'^\d{5}(-\d{4})?$', self.s))

    def task6(self):
        return bool(re.match(r'^[a-z0-9_-]{6,12}$', self.s))

    def task7(self):
        return bool(re.match(r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$', self.s))

    def task8(self):
        return bool(re.match(r'^\d{3}-\d{2}-\d{4}$', self.s))

    def task9(self):
        return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$', self.s))
