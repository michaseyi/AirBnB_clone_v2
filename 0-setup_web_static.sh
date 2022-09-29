#!/usr/bin/env bash
# sets up a web server for development of web_static

#install nginx
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get install nginx
fi

#make necessary directories
mkdir -p /data/web_static/releases/test
echo "/hbnb_static/index.html" > /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared
ln -sf -T  /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data

#nginx config
config="\
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.nginx-debian.html;
    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}"
echo "$config" > /etc/nginx/sites-available/default
service nginx restart

