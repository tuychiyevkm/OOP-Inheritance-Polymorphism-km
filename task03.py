class User:
    def __init__(self, username):
        self.username = username

    def access_level(self):
        pass

class Admin(User):
    def access_level(self):
        return f"{self.username}: Full Access"

class Guest(User):
    def access_level(self):
        return f"{self.username}: Limited Access"

users = [Admin("admin123"), Guest("guest001")]
for u in users:
    print(u.access_level())
