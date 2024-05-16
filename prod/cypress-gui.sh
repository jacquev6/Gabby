#!/bin/bash

set -o errexit
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


if [ -z $DISPLAY ]
then
  DISPLAY=:0 xhost +
  display_option="--env DISPLAY=host.docker.internal:0"
else
  xhost +
  display_option="--env DISPLAY"
fi

docker compose exec \
  $display_option \
  tester-shell \
    npx cypress open \
      --e2e \
      --env IS_PROD_PREVIEW=true \
      --config baseUrl=http://fanout:8090/
