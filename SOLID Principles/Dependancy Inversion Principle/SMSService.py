from NotificationChannel import NotificationChannel

class SMSService(NotificationChannel):
    def send(self, message: str):
        print(f'Sending SMS: {message}')