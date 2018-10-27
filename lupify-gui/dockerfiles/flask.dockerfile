FROM centos:latest

#RUN pip install flask
#RUN pip install flask_login
#RUN pip install pymongo
#RUN pip install flask_wtf
RUN yum clean all
RUN yum update -y
RUN yum install epel-release -y
RUN yum install nginx -y
RUN yum install python2-pip -y
RUN yum install python34 -y
RUN yum install python34-pip -y
RUN yum install python34-devel -y
RUN yum install gcc -y
RUN pip2 install supervisor
RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install flask_login
RUN pip3 install flask_wtf
RUN pip3 install pymongo
RUN pip3 install uwsgi
RUN pip3 install ConfigParser
RUN pip3 install ldap3

RUN yum remove python2-pip -y
RUN yum remove python34-pip -y
RUN yum remove gcc -y
RUN yum remove epel-release -y
#RUN rm -rf /usr/bin/python
#RUN ln -s /usr/bin/python3 /usr/bin/python

RUN rm /etc/nginx/nginx.conf
#RUN rm /etc/nginx/conf.d/default.conf
#RUN rm /etc/nginx/conf.d/*

COPY configs/nginx.conf /etc/nginx/
COPY configs/uwsgi-nginx.conf /etc/nginx/conf.d/

COPY configs/certificate.pem /etc/pki/tls/certs/
COPY configs/key.pem /etc/pki/tls/private/

COPY configs/supervisord.conf /etc/supervisord/supervisord.conf

COPY ./lupify /lupify

COPY scripts/config_script.sh /tmp/

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/bin/bash", "/tmp/config_script.sh"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord/supervisord.conf"]