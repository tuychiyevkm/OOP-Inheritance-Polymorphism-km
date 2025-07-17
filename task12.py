class User:
    def __init__(self, username):
        self.username = username

    def get_dashboard(self):
        pass

class Student(User):
    def get_dashboard(self):
        return f"{self.username}: Course list and progress"

class Instructor(User):
    def get_dashboard(self):
        return f"{self.username}: Teaching dashboard and stats"

users = [Student("student001"), Instructor("prof_said")]
for u in users:
    print(u.get_dashboard())
