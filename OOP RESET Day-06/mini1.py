class audio:
    def play(self):
        return ("Playing Audio")

class video:
    def play(self):
        return ("Playing Video")

a1=audio()
v1=video()
media=[a1,v1]
for i in media:
    print(i.play())
