#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


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

if (cd ../..; git grep -n '\.only' -- frontend)
then
  false
fi

../docker-compose.sh exec \
  $console_options \
  frontend-shell \
    npx cypress run \
      --component "$@"

# Cypress puts screenshots in a different place when invoked with --spec. Fix that.
for d in $(find ../../frontend/cypress/screenshots -maxdepth 1 -name 'TricolorSection*.cy.*')
do
  mkdir -p ../../frontend/cypress/screenshots/adapted/components
  mv $d ../../frontend/cypress/screenshots/adapted/components
done
