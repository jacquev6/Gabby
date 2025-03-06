#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


../docker-compose.sh exec backend-shell \
  mypy \
    --follow-imports silent \
    --strict \
    gabby/adaptation/__init__.py
