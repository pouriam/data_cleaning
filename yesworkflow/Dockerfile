FROM debian:12

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates

# Install Java 22 from Amazon Corretto
RUN wget -O /tmp/corretto.key https://apt.corretto.aws/corretto.key
RUN gpg --dearmor -o /usr/share/keyrings/corretto-archive-keyring.gpg /tmp/corretto.key
RUN echo "deb [signed-by=/usr/share/keyrings/corretto-archive-keyring.gpg] https://apt.corretto.aws stable main" | tee /etc/apt/sources.list.d/corretto.list

RUN apt-get update && apt-get install -y java-22-amazon-corretto-jdk
ENV JAVA_HOME=/usr/lib/jvm/java-22-amazon-corretto


# Install graphviz
RUN apt-get install -y graphviz


# Download the yesworkflow JAR
RUN wget -O /usr/local/bin/yesworkflow.jar https://github.com/yesworkflow-org/yw-prototypes/releases/download/v0.2.0/yesworkflow-0.2.0-jar-with-dependencies.jar

# Write an alias to /etc/profile, so it's available to all users
RUN echo "alias yw='java -jar /usr/local/bin/yesworkflow.jar'" >> /etc/profile.d/yw.sh
RUN echo "if [ -f /etc/profile.d/yw.sh ]; then . /etc/profile.d/yw.sh; fi" >> /etc/bash.bashrc


ENTRYPOINT ["java", "-jar", "/usr/local/bin/yesworkflow.jar"]

