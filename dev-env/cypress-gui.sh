#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


xhost +
docker compose exec \
  --env DISPLAY \
  frontend \
    npx cypress open \
      --config baseUrl=http://fanout:8080/
