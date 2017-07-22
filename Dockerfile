# A basic apache server. To use either add or bind mount content under /var/www
FROM ubuntu:xenial

RUN apt-get update
RUN apt-get purge usbip* libusbip*
RUN apt-get install -y linux-tools-generic module-init-tools linux-image-generic hwdata autossh
#RUN depmod
#RUN modprobe usbip_host
RUN echo 'usbip_host' >> /etc/modules
#RUN /usr/lib/linux-tools/`uname -r`/usbipd
RUN which usbip

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY bind-usb.py /usr/local/bin/bind-usb.py
RUN chmod +x /usr/local/bin/bind-usb.py

ENV \
    TERM=xterm \
    AUTOSSH_LOGFILE=/dev/stdout \
    AUTOSSH_GATETIME=30         \
    AUTOSSH_POLL=10             \
    AUTOSSH_FIRST_POLL=30       \
    AUTOSSH_LOGLEVEL=1

CMD ["/usr/local/bin/bind-usb.py"]
