#! -*- enconding: utf-8 -*-
from flask import Flask, render_template
from flask import request

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static/')
messages = ""

@app.route('/')
def index():
    global messages
    return render_template('index.html', messages=messages)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    global messages
    msg = request.form['message_input']
    messages += "YOU: " + msg + "\n"
    messages += "BOT: " + chatbot_response(msg) + "\n"
    return render_template('index.html', messages=messages)
    
def chatbot_response (msg):
    # PUT CHATBOT CODE HERE
    return 'hi'
    
    
# run the server
if __name__ == '__main__':
  app.debug = True
  app.run()
  
  