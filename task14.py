class User:
    def __init__(self, username):
        self.username = username

    def interact(self):
        pass

class Applicant(User):
    def interact(self):
        return f"{self.username} applied for a job"

class Employer(User):
    def interact(self):
        return f"{self.username} posted a job"

users = [Applicant("user99"), Employer("companyHR")]
for u in users:
    print(u.interact())
