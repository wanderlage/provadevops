FROM python:3
#Creating folders for apps #
RUN mkdir -p /usr/src/app/api
RUN mkdir -p /usr/src/app/tests
#Add requiriments for instalation in python#
ADD ./requirements.txt /usr/src/app/requirements.txt

COPY src/api/* /usr/src/app/api/
COPY src/tests/* /usr/src/app/tests/

RUN pip install -r /usr/src/app/requirements.txt

WORKDIR /usr/src/app

CMD [ "python","./api/app.py" ]