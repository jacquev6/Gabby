#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


console_options="--env ELECTRON_ENABLE_LOGGING=1"
specs_options=""
while [ $# -gt 0 ]
do
  case "$1" in
    --no-console)
      console_options=""
      shift
      ;;
    --visual)
      specs_options="--spec e2e-tests/demo.cy.ts,e2e-tests/visual-appearance.cy.ts,e2e-tests/user-doc.cy.ts"
      shift
      ;;
    *)
      break
      ;;
  esac
done

test_dir=frontend/e2e-tests

if (cd ..; git grep -n '\.only' -- $test_dir)
then
  false
fi

./docker-compose.sh exec \
  $console_options \
  frontend-shell \
    npx cypress run \
      --e2e $specs_options "$@"

if [ -d ../$test_dir/screenshots/user-doc.cy.ts ]
then
  find ../doc/user -name '*.png' -delete
  find ../$test_dir/screenshots/user-doc.cy.ts -name '*.png' | while read line; do
    cp $line ../doc/user/${line#../$test_dir/screenshots/user-doc.cy.ts/}
  done
fi
