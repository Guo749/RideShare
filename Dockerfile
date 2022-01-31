FROM python:3.9-bullseye
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN sed /etc/apt/sources.list && \
    apt-get update && apt-get install -y \
    bash \
    git \
    curl \
    gcc \
    python3-dev\ 
    libpq-dev \
    && curl -fsSL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs \
    && npm install --global yarn \
    && yarn global add @vue/cli-init \
    && yarn global add @vue/cli \
    && rm -rf /tmp/*
  
COPY requirements.txt /code/
RUN pip install pip -U && \
  pip install -r requirements.txt
COPY . /code/

ENTRYPOINT ["/code/entrypoint-initenv.sh"]