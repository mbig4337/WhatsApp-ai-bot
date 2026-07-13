   from flask import Flask, request
   import requests
   import google.generativeai as genai
   import os

   app = Flask(__name__)
   WHATSAPP_TOKEN = os.environ.get('WHATSAPP_TOKEN')
   WHATSAPP_PHONE_NUMBER_ID = os.environ.get('WHATSAPP_PHONE_NUMBER_ID')
   VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', 'mysecret123')
   genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
   model = genai.GenerativeModel('gemini-2.0-flash-exp')
   SYSTEM_PROMPT = "You are WhatsAppAI, a friendly assistant. Reply short. You are in united States, US."

   @app.route('/webhook', methods=['GET'])
   def verify():
       if request.args.get('hub.verify_token') == VERIFY_TOKEN:
           return request.args.get('hub.challenge')
       return "Verification failed", 403

   @app.route('/webhook', methods=['POST'])
   def webhook():
       return "ok", 200
