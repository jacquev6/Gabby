#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


./docker-compose.sh exec \
  backend-shell \
    python -m gabby \
      restore-database \
        s3://jacquev6/gabby/prod/backups/gabby-backup-20250106-014206.tar.gz \
        --patch-according-to-settings \
        --yes

if [ "x${1-}" == "x--upgrade" ]
then
  ./docker-compose.sh exec \
    --workdir /app/backend/gabby \
    backend-shell \
      alembic upgrade head

  ./docker-compose.sh exec \
    backend-shell \
      python -m gabby \
        dump-database-as-unit-tests \
  >../backend/gabby/prod_data_as_unit_tests.py
fi

./docker-compose.sh exec \
  backend-shell \
    python -m gabby \
      sudo import create-user \
        jacquev6+gabby-dev-admin@gmail.com \
        --username admin \
        --password password
