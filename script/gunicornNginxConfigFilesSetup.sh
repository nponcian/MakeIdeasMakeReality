#!/bin/bash

# PURPOSE
# Automate the error-prone process of setting up the necessary configuration files needed by Gunicorn
# and Nginx.

# USAGE
#     bash /absolute/path/from/literally/anywhere/to/script/gunicornNginxConfigFilesSetup.sh
#     or
#     bash ../relative/path/from/literally/anywhere/to/script/gunicornNginxConfigFilesSetup.sh
# Flags
#     --changedefault
#         Replace the Nginx listener to the default port 80 to this web application.
#         Without this flag, ports used are reset to the original values.

PROJECT_PATH=$(readlink -f "${BASH_SOURCE}" | xargs dirname | xargs dirname)
CONFIG_PATH="${PROJECT_PATH}/config"
ENVIRONMENT_VARIABLES_PATH="${CONFIG_PATH}/environmentVariables"

GUNICORN_SERVICE="${CONFIG_PATH}/gunicorn.service"
GUNICORN_SOCKET_NAME="gunicorn.socket"
GUNICORN_SOCKET="${CONFIG_PATH}/${GUNICORN_SOCKET_NAME}"

NGINX_CONF_NAME="makeIdeasMakeRealityNginx.conf"
NGINX_CONF="${CONFIG_PATH}/${NGINX_CONF_NAME}"

ORIGINAL_PORT="8000"
UPDATED_PORT="80"

source ${ENVIRONMENT_VARIABLES_PATH}

sudo ln -s ${GUNICORN_SERVICE} ${MIMR_SYSTEMD_PATH}
sudo ln -s ${GUNICORN_SOCKET} ${MIMR_SYSTEMD_PATH}
sudo systemctl enable --now ${GUNICORN_SOCKET_NAME}

sudo ln -s ${NGINX_CONF} ${MIMR_NGINX_SITES_AVAILABLE_PATH}
sudo ln -s ${MIMR_NGINX_SITES_AVAILABLE_PATH}/${NGINX_CONF_NAME} ${MIMR_NGINX_SITES_ENABLED_PATH}
sudo systemctl enable ${MIMR_NGINX_SERVICE}
sudo systemctl start ${MIMR_NGINX}

if [[ $# -eq 1 && "${1}" == "--changedefault" ]]; then
    sed -i 's/listen '${ORIGINAL_PORT}';/listen '${UPDATED_PORT}';/' ${NGINX_CONF}
    sudo rm -rf ${MIMR_NGINX_ENABLED_DEFAULT_CONF}
else
    sed -i 's/listen '${UPDATED_PORT}';/listen '${ORIGINAL_PORT}';/' ${NGINX_CONF}
    sudo ln -s ${MIMR_NGINX_AVAILABLE_DEFAULT_CONF} ${MIMR_NGINX_ENABLED_DEFAULT_CONF}
fi

sudo systemctl restart ${MIMR_NGINX}
