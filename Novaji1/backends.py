import resend
from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings


class ResendEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        resend.api_key = settings.RESEND_API_KEY
        for message in email_messages:
             resend.Emails.send({
                "from": message.from_email,
                "to": message.to,
                "subject": message.subject,
                "html": message.body,
            })
        return len(email_messages)
