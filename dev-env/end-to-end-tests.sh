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

if (cd ..; git grep -n '\.only' -- tests)
then
  false
fi

docker compose exec \
  $console_options \
  frontend-shell \
    npx cypress run \
      --e2e "$@"

docker compose exec \
  $console_options \
  frontend-shell \
    chown -R "$(id -u):$(id -g)" ../tests/screenshots

if [ -d ../tests/screenshots/gabby.cy.js ]
then
  find ../doc/user -name '*.png' -delete
  find ../tests/screenshots/gabby.cy.js -name '*.png' | while read line; do
    cp $line ../doc/user/${line#../tests/screenshots/gabby.cy.js/}
  done
fi

# Happens when using --spec .../visual-appearance.cy.js
if [ -d ../tests/screenshots/visual-appearance.cy.js ]
then
  mkdir -p ../tests/screenshots/gabby
  sudo mv ../tests/screenshots/visual-appearance.cy.js ../tests/screenshots/gabby
fi