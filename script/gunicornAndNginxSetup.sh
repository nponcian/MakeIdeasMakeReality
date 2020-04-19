#!/bin/bash

# PURPOSE
# Automate the error-prone process of setting up the necessary configuration files needed by Gunicorn
# and Nginx.

# USAGE
#     bash /absolute/path/from/literally/anywhere/to/script/gunicornAndNginxSetup.sh
#     or
#     bash ../relative/path/from/literally/anywhere/to/script/gunicornAndNginxSetup.sh

PROJECT_PATH=$(readlink -f "${BASH_SOURCE}" | xargs dirname | xargs dirname)
CONFIG_PATH="${PROJECT_PATH}/config"

GUNICORN_SERVICE="${CONFIG_PATH}/gunicorn.service"
GUNICORN_SOCKET="${CONFIG_PATH}/gunicorn.socket"

NGINX_CONF_NAME="makeIdeasMakeRealityNginx.conf"
NGINX_CONF="${CONFIG_PATH}/${NGINX_CONF_NAME}"

SYSTEMD_PATH="/etc/systemd/system/"
SITES_AVAILABLE_PATH="/etc/nginx/sites-available/"
SITES_ENABLED_PATH="/etc/nginx/sites-enabled/"

sudo ln -s ${GUNICORN_SERVICE} ${SYSTEMD_PATH}
sudo ln -s ${GUNICORN_SOCKET} ${SYSTEMD_PATH}
systemctl enable --now gunicorn.socket

sudo ln -s ${NGINX_CONF} ${SITES_AVAILABLE_PATH}
sudo ln -s ${SITES_AVAILABLE_PATH}/${NGINX_CONF_NAME} ${SITES_ENABLED_PATH}
systemctl enable nginx.service
systemctl start nginx
systemctl restart nginx
