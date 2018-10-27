#!/bin/bash

set -e

sed -i s/HTTP_PORT_TMP/${LUPIFY_HTTP_PORT}/g /etc/nginx/conf.d/uwsgi-nginx.conf 
sed -i s/HTTPS_PORT_TMP/${LUPIFY_HTTPS_PORT}/g /etc/nginx/conf.d/uwsgi-nginx.conf

exec "$@"
