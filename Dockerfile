# Command to build:
# docker build --build-arg NPM_TOKEN=$NPM_TOKEN .

FROM    omniex/omniex-quickfix:2.0

ARG     NPM_TOKEN
ENV     NPM_TOKEN ${NPM_TOKEN}

RUN     apt-get update && \
        apt-get install -y libxml2-dev libz-dev python && \
        rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY    . .

RUN     npm install --build-from-source
