# Command to build:
# docker build --build-arg NPM_TOKEN=<NPM_TOKEN> .

ARG NPM_TOKEN

FROM omniex/omniex-quickfix:1.0 as build

# Release
FROM amazonlinux:2

ARG NPM_TOKEN
ENV NPM_TOKEN ${NPM_TOKEN}

WORKDIR /home/node

RUN yum -q -y update &&\
    yum install -q -y tar gzip make gcc-c++

COPY --from=build /usr/include/quickfix /usr/include/quickfix
COPY --from=build /usr/lib/libquickfix.so /usr/lib/libquickfix.so

COPY . .

RUN ln -s /usr/lib64/libxml2.so.2 /usr/lib64/libxml2.so &&\
    ln -s /usr/lib64/libz.so.1 /usr/lib64/libz.so

RUN touch /root/.bashrc && \
    curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash && \
    source /root/.bashrc && \
    nvm install 8.16.0 && \
    nvm use 8.16.0 && \
    # creates /lib64/libquickfix.so.17
    npm install --build-from-source
