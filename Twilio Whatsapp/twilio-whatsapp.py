from twilio.rest import Client
from flask import Flask, request
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

# replace to and from numbers as per requirement
FROM_NUMBER = 'whatsapp:+14155238886'
TO_NUMBER = 'whatsapp:+918791335061'


def send_whatsapp_message(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=FROM_NUMBER,
        body=message,
        to=TO_NUMBER
    )
    return message.sid

send_whatsapp_message("Hello World")


# flask server to receive webhook from twilio
app = Flask(__name__)

@app.route('/twilio', methods=['POST'])
def twilio():
    status = request.values.get('SmsStatus')
    tonum = request.values.get('To')
    msgid = request.values.get('MessageSid')
    Body = request.form.get('Body')

    datadict = {'status': status, 'tonum': tonum, 'msgid': msgid, 'message_text': Body}

    if status == 'received':
        # add your logic here
        send_whatsapp_message(datadict['message_text'])

    return datadict


if __name__ == '__main__':
    app.run()
