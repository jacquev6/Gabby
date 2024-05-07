#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


DISPLAY=:0 xhost +
docker compose exec \
  --env DISPLAY=host.docker.internal:0 \
  --env ELECTRON_EXTRA_LAUNCH_ARGS=disable-features=OutOfBlinkCors `# https://github.com/cypress-io/cypress/issues/8399#issuecomment-682004348 to access iframe with Data URL` \
  frontend-shell \
    npx cypress open
