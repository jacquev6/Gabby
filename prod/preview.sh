#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


./build.sh preview false

echo "Gabby prod-preview: start"
docker compose up --remove-orphans --detach
docker compose logs --follow || true

echo "Gabby prod-preview: clean-up"
docker compose down --remove-orphans
docker compose rm --stop --volumes --force
