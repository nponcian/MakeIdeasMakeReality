# PURPOSE
# Exports all environment variables defined within the config file, making them available within the
# current shell and all the spawned child shells. Useful if running the django app through the
# default django provided server via manage.py runserver since the settings are already dependent
# on the environment variables which are only set when using Gunicorn server.

# USAGE
#     cd /path/to/makeIdeasMakeReality/
#     source script/environmentVariablesExporter.sh
# This should be sourced <source file> from target shell instance. Running this as a child shell
# such as commands <./file> or <bash file> would not have any effects since the exported variables
# would not reflect on the calling (parent) shell.

ENVIRONMENT_VARIABLES_PATH="config/environmentVariables"

while read line; do
    export ${line}
done < ${ENVIRONMENT_VARIABLES_PATH}
