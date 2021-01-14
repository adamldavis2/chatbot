
FROM python:3.8

EXPOSE 5000

WORKDIR /chatbot/src/

COPY src/ ./

RUN pip install tensorflow keras nltk
RUN pip install flask
RUN python setup.py

CMD ["python", "main.py"]
