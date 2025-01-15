import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_notification(to_email: str, subject: str, body: str):
    msg = MIMEMultipart()
    msg['From'] = 'your-email@gmail.com'
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your-email@gmail.com', 'your-email-password')
        text = msg.as_string()
        server.sendmail('your-email@gmail.com', to_email, text)
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
