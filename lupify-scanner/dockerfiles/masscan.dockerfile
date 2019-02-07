FROM centos:latest

RUN yum clean all
RUN yum update -y
RUN yum install epel-release -y
RUN yum install masscan -y

#COPY configs/uwsgi-nginx.conf /etc/nginx/conf.d/

#EXPOSE 443

#ENTRYPOINT ["/bin/bash", "/tmp/config_script.sh"]
#CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord/supervisord.conf"]