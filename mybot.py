from flask import Flask, request
from dotenv import load_dotenv
import os
from pymessenger import Bot
app = Flask(__name__)

load_dotenv()
VERIFIER_JETON = os.environ.get('VERIFIER_JETON')
PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN')
FB_API_URL = 'https://graph.facebook.com/v10.0/me/messages?access_token='+PAGE_ACCESS_TOKEN

# make connection to graph api
bot = Bot(PAGE_ACCESS_TOKEN)


def verify_webhook(req):
    """Cette fonction permet de vérifier que le jeton passé correspond à celui sur le webhook
         paramètres:
             req: la requête envoyée au bot de messagerie
         revenir:
             renvoie une chaîne indiquant le succès de la connexion, sinon le jeton est incorrect.
    """
    if req.args.get("hub.verify_token") == VERIFIER_JETON:
        return req.args.get("hub.challenge")
    else:
        return "incorrect token"

def process_message(message):
    """Cette fonction permet de traiter les messages envoyés à la page et la réponse du bot à l'expéditeur
        paramètres:
            message: le message envoyé par le client
        revenir:
            réponse: réponse envoyée par le bot au client
    """

    # convertir le message en minuscules pour un traitement facile
    formatted_message = message.lower()

    if formatted_message == "test":
        response = "Test réussi"
    else:
        response = "Bienvenue sur notre page."

    return response

@app.route("/webhook", methods=["POST", "GET"])
def webhook():
    """C'est la fonction principale utilisée par flask pour
     écouter au point de terminaison `/ webhook`"""
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

            return "Message reçu."

        else:
            return "200"
    
