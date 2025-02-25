#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


backend/all-tests.sh

frontend/all-tests.sh

./end-to-end-tests.sh
