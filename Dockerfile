FROM python:3

RUN apt update
RUN apt install build-essential nginx --yes

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV LISTEN_PORT 80
ENV NGINX_MAX_UPLOAD 0
ENV PYTHONUNBUFFERED=1
#ENV USER_NAME=uwsgi

ARG USER_NAME
RUN useradd -ms /bin/bash ${USER_NAME}

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

COPY start.sh /start.sh
RUN chmod +x /start.sh

COPY . /app
WORKDIR /app


CMD ["/start.sh"]