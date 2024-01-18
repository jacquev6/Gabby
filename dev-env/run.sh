#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


# https://docs.docker.com/compose/reference/
echo "Gabby dev-env: start"
docker compose up --build --remove-orphans --detach
docker compose logs --follow || true
# Clean-up after Ctrl+C
echo "Gabby dev-env: clean-up"
docker compose rm --stop --volumes --force
