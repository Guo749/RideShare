#!/bin/bash

set -e

echo ${COLLECT_STATIC}
if [ "x${COLLECT_STATIC}" = "xon" ]; then
    echo "collect static resources"
    cd ./ridefront/ && yarn install &&  yarn build && cd -
fi


echo "run migrate in background"
/bin/bash /code/db-update.sh &
exec "$@"