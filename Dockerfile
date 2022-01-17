FROM python:3.10-buster

WORKDIR /code
RUN mkdir staticfiles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3.10", "main.py", "requirements.txt" ]