from django.core.mail import EmailMessage

def send_reset_token_by_email(email, token):

    url = f"http://127.0.0.1:8000/account/password/change/?reset_token={token}"

    message = EmailMessage(
        subject = "Password R   eset",
        body= f"Click the link to reset your password {url}",
        to=[email]
    )
    message.send()