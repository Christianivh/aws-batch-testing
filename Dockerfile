
FROM phusion/baseimage:0.11

# ARG DBUSER
# ARG DBPASSWORD
# ARG DBHOST

# ENV USER=$DBUSER
# ENV PASSWORD=$DBPASSWORD
# ENV HOST=$DBHOST
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PYTHON_VERSION 3.7

RUN set -x \
  && apt-get update \
  && apt-get install -y python${PYTHON_VERSION} \
  && apt-get install -y python3-pip  \
  && apt-get clean

WORKDIR /home/

COPY . .

RUN chmod +x /home/script-run.sh
ENTRYPOINT ["sh","/home/script-run.sh"]
CMD []
