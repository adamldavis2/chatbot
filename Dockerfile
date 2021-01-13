
FROM python:3.8

EXPOSE 5000

WORKDIR /chatbot/

COPY src/ src/
COPY static/ static/
COPY templates/ templates/

RUN pip install tensorflow keras nltk
RUN pip install flask

CMD ["python", "src/main.py"]
