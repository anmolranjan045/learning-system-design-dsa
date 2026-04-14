from NotificationChannel import NotificationChannel

class NotificationService:
    def __init__(self, channel: NotificationChannel):
        self.channel = channel
    
    def notify(self, message: str):
        self.channel.send(message)