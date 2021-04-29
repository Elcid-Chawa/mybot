from flask import Flask, request

from pymessenger import Bot
app = Flask(__name__)

VERIFY_TOKEN = 'some-verify-token'# <paste your verify token here>
PAGE_ACCESS_TOKEN = 'EAALQwNvlnS8BAGtpmj2un7fHGQlWrbVFEvvPuRvr8EP1ZB7i4A7ze1n6U4VHOF2lJK99eazVO3846Y3UjiSEXp6ZBNhmZCsJDUL0YrROHGdfyF6pZB8rNecsn8mPpqh061zOI2hQy0ZAG7ubG3dQ185iHMx21b8J7yDZCyX0w1wQZDZD'
FB_API_URL = 'https://graph.facebook.com/v10.0/me/messages?access_token='+PAGE_ACCESS_TOKEN

bot = Bot(PAGE_ACCESS_TOKEN)

def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"

def process_message(message):
    formatted_message = message.lower()
    if formatted_message == "test":
        response = "Test Sucessfull"
    else:
        response = "Welcome to our page."

    return response

@app.route("/webhook", methods=["POST", "GET"])
def webhook():
    """This is the main function flask uses to 
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return verify_webhook(request)
    elif request.method == "POST":
        payload = request.json
        event = payload['entry'][0]['messaging']

        for msg in event:
            text = msg['message']['text']
            sender_id = msg['sender']['id']

            response = process_message(text)
            bot.send_text_message(sender_id, response)

            return "Message received."

        else:
            return "200"
    
