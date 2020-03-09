FROM python:3.6-buster 
RUN pip3 install Flask
RUN pip3 install flask-mysqldb
RUN pip3 install requests
RUN pip3 install redis
RUN mkdir microservice

ADD /microservice /microservice/
ENV FLASK_APP=microservice

ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0 