from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import smtplib
import os
from .utilities.toolbox import ToolBox


class EmailHandler:

    def __init__(
        self,
        receiver_email,
        templates_dir="templates"
    ):
        self.smtp_host = os.environ.get("SMTP_HOST")
        self.smtp_port = int(os.environ.get("SMTP_PORT"))
        self.brand_name = os.environ.get("BRAND_NAME")
        self.company_email = os.environ.get("COMPANY_EMAIL")
        self.smtp_password = os.environ.get("EMAIL_PASSWORD")

        template_path = Path(__file__).parent/templates_dir
        self.jinja_environment = Environment(
            loader=FileSystemLoader(
                str(template_path)
            ),
            autoescape=True
        )
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
        email["from"] = f"{self.brand_name} <{self.company_email}>"
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
        html_template = self._render_template(
            template_name=template_name,
            context=context
        )

        #create message
        email_message = self._generate_message(
            to_email=to_email,
            subject=subject,
            html_body=html_template,
            body=body
        )

        return email_message 

    #     #send email
    #     try:
        
    #         with smtplib.SMTP(self.smtp_host, port=self.smtp_port) as connection:
                
    #             connection.ehlo()
    #             connection.starttls()
    #             connection.ehlo()

    #             if self.smtp_password:  
    #                 connection.login(
    #                     user=self.sender_email,
    #                     password=self.smtp_password
    #                 )
    #             connection.send_message(email_message)

    #     except smtplib.SMTPAuthenticationError:
    #         print("SMTP authentication failed.")
    #         return False

    #     except smtplib.SMTPConnectError:
    #         print("Could not connect to SMTP server")
    #         return False

    #     except Exception as error:
    #         print(f"Email forwarding failed: {error}")
    #         return False

    def send_otp(self, otp_object):


        tb = ToolBox(
            dict_or_json=otp_object
        )

        otp = tb.retrieve_structure_values("otp")
        expires_at = tb.retrieve_structure_values("expiresAt")
        client_name = tb.retrieve_structure_values("clientName")
        subject = tb.retrieve_structure_values("subject")

        message = f""" 
            Dear Client, 

            please use the following one time password to verify
            your email address:

                        OTP: {otp}

            if you did not request the OTP please ignore this email

            Be well,
            {client_name}

        """

        email_context = {
            "otp":otp,
            "sender_name":self.brand_name,
            "expires_at":expires_at.strftime("%H:%M")
        }
        
        self.send_email(
            to_email=self.receiver_email,
            subject=subject,
            template_name="emails/otp.html",
            context=email_context,
            body=message
        )

        # return {
        #     "success": True,
        #     "otp": otp,
        #     "message":"OTP sent successfully"
        # }

