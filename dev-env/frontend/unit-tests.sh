#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


console_options=""
while [ $# -gt 0 ]
do
  case "$1" in
    --console)
      console_options="--env ELECTRON_ENABLE_LOGGING=1"
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
      --component "$@"
