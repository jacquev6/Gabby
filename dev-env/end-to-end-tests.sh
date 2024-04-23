#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


console_options="--env ELECTRON_ENABLE_LOGGING=1"
while [ $# -gt 0 ]
do
  case "$1" in
    --no-console)
      console_options=""
      shift
      ;;
    *)
      break
      ;;
  esac
done

docker compose exec \
  $console_options \
  frontend-shell \
    npx cypress run \
      --e2e "$@"

if [ -f end-to-end-tests.app.sh ]
then
  ./end-to-end-tests.app.sh
fi
