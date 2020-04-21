#!/bin/bash

# PURPOSE
# Automate the error-prone process of setting up the necessary configuration files needed by Gunicorn
# and Nginx.

# USAGE
#     bash /absolute/path/from/literally/anywhere/to/script/gunicornNginxConfigFilesSetup.sh
#     or
#     bash ../relative/path/from/literally/anywhere/to/script/gunicornNginxConfigFilesSetup.sh

PROJECT_PATH=$(readlink -f "${BASH_SOURCE}" | xargs dirname | xargs dirname)
CONFIG_PATH="${PROJECT_PATH}/config"
ENVIRONMENT_VARIABLES_PATH="${CONFIG_PATH}/environmentVariables"

GUNICORN="gunicorn"
GUNICORN_SERVICE_NAME="${GUNICORN}.service"
GUNICORN_SERVICE="${CONFIG_PATH}/${GUNICORN_SERVICE_NAME}"
GUNICORN_SOCKET_NAME="${GUNICORN}.socket"
GUNICORN_SOCKET="${CONFIG_PATH}/${GUNICORN_SOCKET_NAME}"

NGINX_CONF_NAME="makeIdeasMakeRealityNginx.conf"
NGINX_CONF="${CONFIG_PATH}/${NGINX_CONF_NAME}"

ORIGINAL_PORT="8000"
UPDATED_PORT="80"

restartGunicorn()
{
    sudo systemctl daemon-reload
    sudo systemctl stop ${GUNICORN_SERVICE_NAME} # or simply # ${GUNICORN}
    sudo systemctl stop ${GUNICORN_SOCKET_NAME}
    sudo systemctl start ${GUNICORN_SERVICE_NAME}
    sudo systemctl start ${GUNICORN_SOCKET_NAME}
    sudo systemctl restart ${GUNICORN_SERVICE_NAME}
    sudo systemctl restart ${GUNICORN_SOCKET_NAME}
}

restartNginx()
{
    sudo systemctl daemon-reload
    sudo systemctl stop ${MIMR_NGINX}
    sudo systemctl start ${MIMR_NGINX}
    sudo systemctl restart ${MIMR_NGINX}
}

setupGunicorn()
{
    sudo ln -s -f ${GUNICORN_SERVICE} ${MIMR_SYSTEMD_PATH}
    sudo ln -s -f ${GUNICORN_SOCKET} ${MIMR_SYSTEMD_PATH}
    echo "Done linking ${GUNICORN} config files"

    sudo systemctl enable --now ${GUNICORN_SOCKET_NAME}
    echo "Done enabling ${GUNICORN} to automatically start on boot"

    restartGunicorn # Not necessary, but to always be sure that all changes would reflect
    echo "Done restarting ${GUNICORN}"

    echo -n "${GUNICORN_SERVICE_NAME} MainPID: "
    systemctl show --value -p MainPID ${GUNICORN_SERVICE_NAME}
    echo "Done processing ${GUNICORN} service"
}

setupNginx()
{
    sudo ln -s -f ${NGINX_CONF} ${MIMR_NGINX_SITES_AVAILABLE_PATH}
    sudo ln -s -f ${MIMR_NGINX_SITES_AVAILABLE_PATH}/${NGINX_CONF_NAME} ${MIMR_NGINX_SITES_ENABLED_PATH}
    echo "Done linking ${MIMR_NGINX} config files"

    sudo systemctl enable ${MIMR_NGINX_SERVICE}
    echo "Done enabling ${MIMR_NGINX} to automatically start on boot"

    echo "Use port ${UPDATED_PORT}? [y/n]"
    echo -n "---> Input: "
    read shouldUseUpdatedPort

    # if [[ $# -eq 1 && "${1}" == "--changedefault" ]]; then
    if [[ "${shouldUseUpdatedPort}" == "y" || "${shouldUseUpdatedPort}" == "Y" ]]; then
        echo "Port ${UPDATED_PORT} would be used"
        sed -i 's/listen '${ORIGINAL_PORT}';/listen '${UPDATED_PORT}';/' ${NGINX_CONF}
        sudo rm -rf ${MIMR_NGINX_ENABLED_DEFAULT_CONF}
    else
        echo "Port ${ORIGINAL_PORT} would be used"
        sed -i 's/listen '${UPDATED_PORT}';/listen '${ORIGINAL_PORT}';/' ${NGINX_CONF}
        sudo ln -s -f ${MIMR_NGINX_AVAILABLE_DEFAULT_CONF} ${MIMR_NGINX_ENABLED_DEFAULT_CONF}
    fi

    restartNginx
    echo "Done restarting ${MIMR_NGINX} service"

    echo "Done processing ${MIMR_NGINX} service"
}

source ${ENVIRONMENT_VARIABLES_PATH}
setupGunicorn
setupNginx
