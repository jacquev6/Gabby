#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


frontend/shell.sh -c 'npx cypress run --e2e --config baseUrl=http://fanout:8081/'
rm -rf ../doc/user
mkdir -p ../doc/user
cp ../frontend/cypress/screenshots/*/doc/*.png ../doc/user
