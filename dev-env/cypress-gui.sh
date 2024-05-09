#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


DISPLAY=:0 xhost +
docker compose exec \
  --env DISPLAY=host.docker.internal:0 \
  frontend-shell \
    npx cypress open
