FROM zenika/alpine-chrome

USER root
RUN apk add --no-cache chromium-chromedriver
USER chrome
ENTRYPOINT ["chromedriver","--allowed-ips=","--allowed-origins=*"]









# FROM python:alpine
#
# RUN apk add bash-completion
#
# # CMD ["/bin/bash"]
#
# # RUN wget https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip  \
# #     && unzip -d /usr/local/bin chromedriver_linux64.zip
#
# RUN apk upgrade --no-cache --available \
#     && apk add --no-cache \
#       chromium \
#       ttf-freefont \
#       font-noto-emoji \
#     && apk add --no-cache \
#       --repository=https://dl-cdn.alpinelinux.org/alpine/edge/testing \
#       font-wqy-zenhei
# COPY local.conf /etc/fonts/local.conf
#
#
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