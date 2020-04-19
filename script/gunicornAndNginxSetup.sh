#!/bin/bash

# PURPOSE
# Automate the error-prone process of setting up the necessary configuration files needed by Gunicorn
# and Nginx.

# USAGE
#     bash /absolute/path/from/literally/anywhere/to/script/gunicornAndNginxSetup.sh
#     or
#     bash ../relative/path/from/literally/anywhere/to/script/gunicornAndNginxSetup.sh
# Flags
#     --changedefault
#         Replace the Nginx listener to the default port 80 to this web application.
#         Without this flag, ports used are reset to the original values.


PROJECT_PATH=$(readlink -f "${BASH_SOURCE}" | xargs dirname | xargs dirname)
CONFIG_PATH="${PROJECT_PATH}/config"

GUNICORN_SERVICE="${CONFIG_PATH}/gunicorn.service"
GUNICORN_SOCKET="${CONFIG_PATH}/gunicorn.socket"

NGINX_CONF_NAME="makeIdeasMakeRealityNginx.conf"
NGINX_CONF="${CONFIG_PATH}/${NGINX_CONF_NAME}"

SYSTEMD_PATH="/etc/systemd/system/"
SITES_AVAILABLE_PATH="/etc/nginx/sites-available/"
SITES_ENABLED_PATH="/etc/nginx/sites-enabled/"
DEFAULT_AVAILABLE_NGINX_CONF="/etc/nginx/sites-available/default"
DEFAULT_ENABLED_NGINX_CONF="/etc/nginx/sites-enabled/default"

ORIGINAL_PORT="8000"
UPDATED_PORT="80"

sudo ln -s ${GUNICORN_SERVICE} ${SYSTEMD_PATH}
sudo ln -s ${GUNICORN_SOCKET} ${SYSTEMD_PATH}
sudo systemctl enable --now gunicorn.socket

sudo ln -s ${NGINX_CONF} ${SITES_AVAILABLE_PATH}
sudo ln -s ${SITES_AVAILABLE_PATH}/${NGINX_CONF_NAME} ${SITES_ENABLED_PATH}
sudo systemctl enable nginx.service
sudo systemctl start nginx

if [[ $# -eq 1 && "${1}" == "--changedefault" ]]; then
    sed -i 's/listen '${ORIGINAL_PORT}';/listen '${UPDATED_PORT}';/' ${NGINX_CONF}
    sudo rm -rf ${DEFAULT_ENABLED_NGINX_CONF}
else
    sed -i 's/listen '${UPDATED_PORT}';/listen '${ORIGINAL_PORT}';/' ${NGINX_CONF}
    sudo ln -s ${DEFAULT_AVAILABLE_NGINX_CONF} ${DEFAULT_ENABLED_NGINX_CONF}
fi

sudo systemctl restart nginx
