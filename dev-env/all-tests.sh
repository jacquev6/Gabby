#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


backend/unit-tests.sh
frontend/unit-tests.sh
./end-to-end-tests.sh
