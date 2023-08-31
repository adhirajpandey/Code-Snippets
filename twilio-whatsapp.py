from twilio.rest import Client
from flask import Flask, request


#replace account_sid and auth_token with your own credentials
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'e09cxxxxxxxxxxxxxxxxxxxxxxx'

#replace to and from numbers as per requirement
def send_whatsapp_message(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14xxxxxxx',
        body=message,
        to='whatsapp:+9187xxxxxxxx'
    )
    return message.sid

# send_whatsapp_message("Hello World")


#flask server to receive webhook from twilio
app = Flask(__name__)

@app.route('/twilio', methods=['POST'])
def twilio():
    status = request.values.get('SmsStatus')
    tonum = request.values.get('To')
    msgid = request.values.get('MessageSid')
    Body = request.form.get('Body')

    datadict = {'status': status, 'tonum': tonum, 'msgid': msgid, 'message_text': Body}

    if status == 'received':
        #add your logic here
        send_whatsapp_message(datadict['message_text'])

    return datadict


if __name__ == '__main__':
    app.run()
