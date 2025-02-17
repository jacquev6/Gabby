#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


../docker-compose.sh exec backend-shell \
  black \
    --line-length 160 \
    gabby/{adaptation,fixtures.py}
