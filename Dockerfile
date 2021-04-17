from python:3.7-slim-stretch


WORKDIR /var-rad_pie_chart

ADD . /var-rad_pie_chart

RUN pip install -r requirements.txt


