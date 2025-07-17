class Notification:
    def __init__(self, recipient):
        self.recipient = recipient

    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        return f"Sending email to {self.recipient}"

class SMSNotification(Notification):
    def send(self):
        return f"Sending SMS to {self.recipient}"

notifs = [EmailNotification("komron@gmail.com"), SMSNotification("+998901234567")]
for n in notifs:
    print(n.send())
