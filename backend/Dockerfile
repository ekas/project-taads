FROM tiangolo/uvicorn-gunicorn:python3.8

COPY . /app

RUN pip3 install -r requirements.txt

WORKDIR /app

EXPOSE 3000

CMD ["python3", "main.py"]