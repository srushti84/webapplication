FROM amazonlinux:latest

RUN yum update -y && \
    yum install -y httpd && \
    yum search wget && \
    yum install wget -y && \
    yum install unzip -y

RUN cd /var/www/html

RUN wget https://github.com/ProductDevelopmentAndDesign/Wool-alert/archive/refs/heads/main.zip

RUN unzip main.zip

RUN cp -r woolalert-main/* /var/www/html/

RUN rm -rf woolalert-main main.zip

EXPOSE 80

