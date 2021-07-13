#!/bin/bash
set -e
# Get the maximum upload file size for Nginx, default to 0: unlimited
USE_NGINX_MAX_UPLOAD=${NGINX_MAX_UPLOAD:-0}
# Generate Nginx config for maximum upload file size
echo "client_max_body_size $USE_NGINX_MAX_UPLOAD;" > /etc/nginx/conf.d/upload.conf


# Get the listen port for Nginx, default to 80
USE_LISTEN_PORT=${LISTEN_PORT:-80}

# Generate Nginx config
echo "server {
    listen ${USE_LISTEN_PORT};
    server_name localhost;
    access_log /var/log/nginx/falcon-app-access.log;
    error_log /var/log/nginx/falcon-app-error.log warn;

    location / {
        uwsgi_pass 127.0.0.1:8080;
        include uwsgi_params;
    }
" > /etc/nginx/conf.d/nginx.conf

# Finish the Nginx config file
echo "}" >> /etc/nginx/conf.d/nginx.conf

exec "$@"