# chatbot

Chatbot prototype in Python

Clone repo: git clone https://github.com/adamldavis2/chatbot.git

## Install

First, install python and run:
```
pip install flask
pip install tensorflow keras nltk
```

## Run

cd chatbot/src

Run the following command: `python main.py`


## Docker

Build

docker build -t chatbot:1 .

Run:

docker run -p 5000:5000 chatbot:1
