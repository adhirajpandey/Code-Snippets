import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv


#funtion to mail the link
def sendMail(user_email, product_title, product_price, product_link):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = os.getenv("SENDER_EMAIL_ID")
        receiver_email = [user_email] 
        password = os.getenv("SENDER_EMAIL_PASSWORD")       
        FROM = f"Price Tracker Bot"
        SUBJECT = f"ALERT!! Price Drop for your Product"
        TEXT = f"""Hey User,

Price of your product which you asked us to track has dropped.

Please check the below details for the same: 

Product - {product_title}
Price - {product_price}
Link - {product_link}

Happy Shopping!!

Regards,
Price Tracker Bot"""
        
        message = 'From: {}\nSubject: {}\n\n{}'.format(FROM,SUBJECT, TEXT)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

            print("Mail Sent Successfully")