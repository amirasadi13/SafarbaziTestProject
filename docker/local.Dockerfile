FROM python:3.9.16-alpine3.17
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN python3 -m pip install --upgrade pip 
ADD requirements/ requirements/
RUN pip install -r requirements/local.txt
COPY .. /app/
