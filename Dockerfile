FROM alpine

# install python and pip
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# install libs
RUN apk update && apk add --no-cache bash alsa-lib at-spi2-atk atk cairo cups-libs dbus-libs eudev-libs expat flac \
        gdk-pixbuf glib libgcc libjpeg-turbo libpng libwebp libx11 libxcomposite libxdamage libxext libxfixes \
        tzdata libexif udev xvfb zlib-dev chromium chromium-chromedriver

# # Install chromedriver
# RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip \
#     && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
#     && rm /tmp/chromedriver_linux64.zip \
#     && chmod 755 /opt/selenium/chromedriver \
#     && ln -fs /opt/selenium/chromedriver /usr/bin/chromedriver

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

# # CMD ["/bin/bash"]

# ENV LANG en_US.UTF-8
# ENV LANGUAGE en_US:en
# ENV LC_ALL en_US.UTF-8
# ENV GLIBC_REPO=https://github.com/sgerrand/alpine-pkg-glibc
# ENV GLIBC_VERSION=2.30-r0
# RUN set -ex && \
#     apk --update add libstdc++ curl ca-certificates && \
#     for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION}; \
#         do curl -sSL ${GLIBC_REPO}/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done && \
#     apk add --allow-untrusted /tmp/*.apk && \
#     rm -v /tmp/*.apk && \
#     /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib
#
# CMD ["/bin/bash"]
#
# # apt-get install libgconf-2-4