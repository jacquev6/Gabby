#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


xhost +
docker compose exec \
  --env DISPLAY \
  preview-tester \
    npx cypress open \
      --e2e \
      --env IS_PROD_PREVIEW=true \
      --config baseUrl=http://preview-fanout:8090/
