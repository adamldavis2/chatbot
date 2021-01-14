
FROM python:3.8

EXPOSE 5000

WORKDIR /chatbot/src/

COPY src/ ./

RUN pip install flask

CMD ["python", "main.py"]
