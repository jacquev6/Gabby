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

if (cd ..; git grep -n 'it\.only' -- tests)
then
  false
fi

docker compose exec \
  $console_options \
  frontend-shell \
    npx cypress run \
      --e2e "$@"

if [ -d ../tests/screenshots/gabby.cy.js ]
then
  find ../doc/user -name '*.png' -delete
  find ../tests/screenshots/gabby.cy.js -name '*.png' | while read line; do
    cp $line ../doc/user/${line#../tests/screenshots/gabby.cy.js/}
  done
fi
