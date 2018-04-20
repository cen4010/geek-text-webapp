FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /webapp
WORKDIR /webapp
EXPOSE 8000
ADD requirements.txt /webapp/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD webapp /webapp/
ADD docker-entrypoint.sh /webapp
ENTRYPOINT /webapp/docker-entrypoint.sh
