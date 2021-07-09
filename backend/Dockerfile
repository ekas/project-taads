FROM tiangolo/uvicorn-gunicorn:python3.8
COPY . .
RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate
RUN pip3 install -r requirements.txt
EXPOSE 4000
CMD ["python3", "main.py"]