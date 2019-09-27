FROM node:alpine
LABEL maintainer="skygragon@gmail.com"

COPY bin/entrypoint /
RUN npm i -g vsc-leetcode-cli

WORKDIR /root
VOLUME ["/root"]
ENTRYPOINT ["/entrypoint"]
