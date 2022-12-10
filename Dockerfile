FROM selenium/standalone-chrome:107.0

# install pip
RUN sudo apt update && \
    sudo apt upgrade -y && \
    sudo apt install pip -y

# install allure
RUN sudo wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.19.0/allure-commandline-2.19.0.tgz \
        -P /usr/local && \
    sudo tar -xvf /usr/local/allure-commandline-2.19.0.tgz -C /usr/local/ && \
    sudo ln -s /usr/local/allure-2.19.0/bin/allure /bin && \
    sudo apt install openjdk-11-jdk -y

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && \
    sudo ln -s /home/seluser/.local/bin/pytest /bin/pytest

EXPOSE 5050:5050

CMD pytest -v --tb=line --alluredir=/home/seluser/allure-results tests ; \
    allure serve -p 5050 /home/seluser/allure-results