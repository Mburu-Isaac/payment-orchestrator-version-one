import os
import smtplib
from email.message import EmailMessage


class NotificationHandler:
    
    def __init__(self):
        pass

    def email_handler(
        self,
        to_email,
        subject,
        body,
        company_name,
        html_structure=None

    ):

        try:

            company_email = os.environ.get("COMPANY_EMAIL")

            email = EmailMessage()
            email["From"] = f"{company_name} <{company_email}>"
            email["To"] = to_email
            email["Subject"] = subject
            email.set_content(body)

            if html_structure:
                email.add_alternative(html_structure, subtype="html")

            with smtplib.SMTP("smtp.gmail.com", port=int(os.getenv("SMTP_PORT"))) as connection:
                connection.starttls()
                connection.login(
                    user=company_email,
                    password=os.getenv("EMAIL_PASSWORD")
                )
                connection.send_message(email)

            return True

        except smtplib.SMTPAuthenticationError:
            print("SMTP authentication failed.")
            return False

        except smtplib.SMTPConnectError:
            print("Could not connect to SMTP server")
            return False

        except Exception as error:
            print(f"Email forwarding failed: {error}")
            return False


