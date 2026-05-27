from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import smtplib
import os


class EmailHandler:

    def __init__(
        self,
        draft,
        receiver_email,
        templates_dir="templates"
    ):
        self.smtp_host = os.environ.get("SMTP_HOST")
        self.smtp_port = int(os.environ.get("SMTP_PORT"))
        self.sender_email = os.environ.get("COMPANY_EMAIL")
        self.sender_name = "ETERNITY"
        self.smtp_password = os.environ.get("EMAIL_PASSWORD")

        template_path = Path(__file__).parent/templates_dir
        self.jinja_environment = Environment(
            loader=FileSystemLoader(
                str(template_path)
            ),
            autoescape=True
        )
        self.draft = draft
        self.receiver_email = receiver_email
    

    def _render_template(
        self,
        template_name,
        context
    ):
        # context.setdefault("year", datetime.now().year)
        template = self.jinja_environment.get_template(template_name)
        return template.render(context)

    def _generate_message(
        self,
        to_email,
        subject,
        html_body,
        body
    ):
        
        email = EmailMessage()
        email["from"] = f"{self.sender_name} <{self.sender_email}>"
        email["to"] = to_email
        email["Subject"] = subject
        email.set_content(body)
        email.add_alternative(html_body, subtype="html")

        return email

    def send_email(
        self,
        to_email,
        subject, 
        template_name,
        context,
        body
    ):
        
        #render template
        html_body = self._render_template(
            template_name=template_name,
            context=context
        )

        #create message
        email_message = self._generate_message(
            to_email=to_email,
            subject=subject,
            html_body=html_body,
            body=body
        )

        #send email
        try:
        
            with smtplib.SMTP(self.smtp_host, port=self.smtp_port) as connection:
                
                connection.ehlo()
                connection.starttls()
                connection.ehlo()

                if self.smtp_password:  
                    connection.login(
                        user=self.sender_email,
                        password=self.smtp_password
                    )
                connection.send_message(email_message)

        except smtplib.SMTPAuthenticationError:
            print("SMTP authentication failed.")
            return False

        except smtplib.SMTPConnectError:
            print("Could not connect to SMTP server")
            return False

        except Exception as error:
            print(f"Email forwarding failed: {error}")
            return False

    def send_otp(self):

        otp, expires_at, message, subject = self.draft._draft_otp()

        email_context = {
            "otp":otp,
            "sender_name":self.sender_name,
            "expires_at":expires_at.strftime("%H:%M")
        }
        
        self.send_email(
            to_email=self.receiver_email,
            subject=subject,
            template_name="emails/otp.html",
            context=email_context,
            body=message
        )

        return {
            "success": True,
            "otp": otp,
            "message":"OTP sent successfully"
        }

    def send_verification_email(self):
        
        verification_link, message, subject, expires_at = self.draft._draft_verification_email()

        email_context = {
            "verification_link": verification_link,
            "expires_at": expires_at,
            "sender_name": self.sender_name
        }

        self.send_email(
            to_email=self.receiver_email,
            subject=subject,
            template_name="emails/verify_email.html",
            context=email_context,
            body=message
        )

        return {
            "success":True,
            "message":"email sent successfully"
        }