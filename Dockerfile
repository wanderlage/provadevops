FROM python:3
#Creating folders for apps #
RUN mkdir -p /usr/src/app/api
RUN mkdir -p /usr/src/app/tests
#Add requiriments for instalation in python#
ADD ./requirements.txt /usr/src/app/requirements.txt
#Copy app for execution local#
COPY src/api/* /usr/src/app/api/
#Install requirements for execute the app#
RUN pip install -r /usr/src/app/requirements.txt
#Local for default workdir#
WORKDIR /usr/src/app
#the execute python app#
CMD [ "python","./api/app.py" ]