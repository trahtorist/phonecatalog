FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/backend
WORKDIR /opt/backend
COPY requirements.txt /opt/backend
RUN pip install -r requirements.txt
EXPOSE 8000
