#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


docker compose exec \
  --env ELECTRON_ENABLE_LOGGING=1 \
  adapted \
    npx cypress run \
      --component "$@"
