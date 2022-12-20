FROM tensorflow/tensorflow

WORKDIR /tensorflow
EXPOSE 80

RUN pip install --upgrade flask
COPY . .

ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0 --port=80
