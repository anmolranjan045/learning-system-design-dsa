from EmailService import EmailService
from SMSService import SMSService
from NotificationService import NotificationService

em = EmailService()
ns1 = NotificationService(em)
ns1.notify('Hello')

sms = SMSService()
ns2 = NotificationService(sms)
ns2.notify('Hello SMS')