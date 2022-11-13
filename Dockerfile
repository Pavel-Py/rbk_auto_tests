FROM alpine

# install python and pip
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# install libs
RUN apk update && apk add --no-cache bash alsa-lib at-spi2-atk atk cairo cups-libs dbus-libs eudev-libs expat flac \
        gdk-pixbuf glib libgcc libjpeg-turbo libpng libwebp libx11 libxcomposite libxdamage libxext libxfixes \
        tzdata libexif udev xvfb zlib-dev chromium chromium-chromedriver

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest", "--alluredir=results", "."]