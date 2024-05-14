import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(email, report):
    devhire_email = 'ashadq345@gmail.com'
    devhire_email_password = 'axax rbmv bgyp dhvw'

    # Create a MIMEMultipart message
    mail_content = MIMEMultipart("alternative")
    mail_content['Subject'] = 'DevHire Interview Report'
    mail_content['From'] = devhire_email
    mail_content['To'] = email

    # HTML content of the email
    html_content = f"""
    <html>
        <body style="background-color: #f4f4f4; font-family: Arial, sans-serif; padding: 20px;">
            <div style="background-color: #ffffff; padding: 20px; border-radius: 10px;">
                <h2 style="color: #333333;">DevHire Interview Report</h2>
                <hr style="border: 1px solid #dddddd;">
                <p>{report}</p>
            </div>
        </body>
    </html>
    """

    # Attach the HTML content to the email
    html_part = MIMEText(html_content, "html")
    mail_content.attach(html_part)

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as server:
        server.login(devhire_email, devhire_email_password)
        server.send_message(mail_content)

# Example usage
# send_mail('recipient@example.com', 'This is a sample report.')