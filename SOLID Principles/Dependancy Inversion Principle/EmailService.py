from NotificationChannel import NotificationChannel

class EmailService(NotificationChannel):
    def send(self, message: str):
        print(f'Sending SMS: {message}')