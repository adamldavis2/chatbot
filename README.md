# chatbot

Chatbot prototype in Python

## Install

First, install python and run:
```
pip install flask
pip install tensorflow keras nltk
```

## Run

Run the following command: `python src/main.py`


## Docker

Build

docker build -t chatbot:1 .

Run:

docker run -p 5000:5000 chatbot:1