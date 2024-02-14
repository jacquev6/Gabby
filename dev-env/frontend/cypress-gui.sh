#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


./shell.sh -c 'npx start-server-and-test "vite --port 4174 --strictPort" http://localhost:4174/ "cypress open --config baseUrl=http://localhost:4174/"'
