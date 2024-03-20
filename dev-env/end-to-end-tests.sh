#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


docker compose exec \
  frontend \
    npx cypress run \
      --e2e "$@"

if [ -f end-to-end-tests.app.sh ]
then
  ./end-to-end-tests.app.sh
fi
