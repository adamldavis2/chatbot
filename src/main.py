#! -*- enconding: utf-8 -*-
from flask import Flask, render_template
from flask import request
import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
import tensorflow as tf
from tensorflow import keras

import json
import random

lemmatizer = WordNetLemmatizer()
model = keras.models.load_model('chatbot_model.h5')
intents = json.loads(open('intents_deductions.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

# Flask

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
    
    
# run the server
if __name__ == '__main__':
  app.debug = True
  app.run()
  
  