class notification:
    def send(self):
        print("Notification sent")

class email(notification):
    def send(self):
        print("Email sent")

class sms(notification):
    def send(self):
        print("SMS sent")

class whatsapp(notification):
    def send(self):
        print("WhatsApp message sent")

notifications = [email(), sms(), whatsapp()]

for n in notifications:
    n.send()

def notify(notification):
    notification.send()
