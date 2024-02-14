#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


frontend/shell.sh -c 'npx start-server-and-test "vite --port 4173 --strictPort" http://localhost:4173/ "cypress run --e2e --config baseUrl=http://localhost:4173/"'
rm -rf ../frontend/public/help
mkdir -p ../frontend/public/help
cp ../frontend/cypress/screenshots/*/help/*.png ../frontend/public/help
