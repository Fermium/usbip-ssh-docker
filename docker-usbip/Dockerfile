FROM ubuntu:xenial

RUN apt-get update

# Remove any trace of the usbip package, we need the one from the kernel tools
RUN apt-get purge usbip* libusbip*
RUN apt-get install -y linux-tools-generic linux-cloud-tools-generic module-init-tools linux-image-generic hwdata autossh
RUN echo 'usbip_host' >> /etc/modules

# Install Python 3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY bind-usb.py /usr/local/bin/bind-usb.py
RUN chmod +x /usr/local/bin/bind-usb.py

EXPOSE 3240

CMD ["/usr/local/bin/bind-usb.py"]
