#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


# https://docs.docker.com/compose/reference/
docker compose up --build --remove-orphans --detach
docker compose logs --follow || true
# Clean-up after Ctrl+C
docker compose rm --stop --volumes --force
