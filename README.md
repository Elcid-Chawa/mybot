# mybot

This is a test messenger bot app build with Python - Flask library. It connects to a facebook page via a token and respose to messages sent by clients to the facebook page.

## Setup Requirements

- Python 3.6 or higher
- Flask
- pymessanger
- ptyhon-dotenv
- [ngrok](https://ngrok.com/download)

## Environment Setup

### Install Libraries
- Install python libraries to run project
```
pip3 install -r requirements.txt
```
- Download [ngrok](https://ngrok.com/download)
- Login to ngrok from your browser.
- Follow instructions [here](https://dashboard.ngrok.com/get-started/setup) to connect to your account from your local machine.

### Facebook App Setup
- Login/Register to [Facebook Developers](https://developers.facebook.com/) site
- Create a new app
![create](imgs/create_app.png)
- Select Business app type then Click *Continue*
![select](imgs/select_type.png)
- Enter app name and Contact email Then click *Create APP*
![select](imgs/app_config.png)
- Select the Product *Messenger* and Click *SetUp*
![product](imgs/add_product.png)
- Create new facebook page or Add an Existing Page where you will use the bot.
![page](imgs/create_page.png)
- Generate an Access Token for the page. Copy and keep this token secrete and do not share with any one.
![token](imgs/generate_token.png)

## Running the App
- We would clone this repo
- Navigate to the project root folder
- create a *.env* file with fields
    - -> VERIFIER_JETON=`"add any verificatio message here"`
    - -> PAGE_ACCESS_TOKEN=`"add the token generated from facebook here"`

- Now run the flask app
```
FLASK_APP=mybot.py flask run
```
![flask](imgs/flask_app.png)
- Navigate to where you downloaded the *ngrok* application and run ngrok.
```
./ngrock http 5000
```
![ngrok](imgs/ngrok.png)
- Copy the Fowarding url with https
```
https://230696fa7855.ngrok.io
```
- Go back to your facebook app settings and Edit the Webhook
![webhook](imgs/webhook.png)
- Insert the url you coppied adding `/webhook` to hit the webhook endpoint served by the app
```
https://230696fa7855.ngrok.io/webhook
```
![verify](imgs/verify_token.png)
- Save the configurations. The webhook config page should close without errors.
- You should see a message from your flask app terminal showing your conncetion was successfull.
![verified](imgs/verified.png)
- Now send a message to your faceboog page and it should respond to you directly.
