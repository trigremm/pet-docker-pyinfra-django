# docker build -t test/openssh .
# MAINTAINER Aleksandar Diklic "https://github.com/rastasheep"

FROM ubuntu:18.04

ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN echo 'root:root' |chpasswd

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN mkdir /root/.ssh

RUN apt-get clean 

EXPOSE 22

CMD    ["/usr/sbin/sshd", "-D"]

# docker run -d -p 10022:22 -p 10080:80 -p 10443:443  test/openssh