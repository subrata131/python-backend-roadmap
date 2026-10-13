class email:
    def send(self,m):
        return (f"Email sent:{m}")

class sms:
    def send(self,m):
        return (f"Sms sent:{m}")

e1=email()
s1=sms()
notification=[e1,s1]

for i in notification:
    print(i.send("Your Order has been shiped"))
