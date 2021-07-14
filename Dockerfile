FROM python:3

RUN apt update && apt install build-essential python-dev nginx --yes &&\
    apt-get clean autoclean &&\
    apt-get autoremove --yes &&\
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

ARG UID=1000
RUN useradd -d /user -l -m -Uu ${UID} -r -s /bin/bash user

COPY nginx.conf /etc/nginx/conf.d/

COPY --chown=${UID}:${UID} . /app

COPY start.sh /start.sh

CMD ["bash", "/start.sh"]