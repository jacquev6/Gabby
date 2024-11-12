#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


set -x

../load-prod-db-backup.sh

../docker-compose.sh exec --workdir /app/backend/gabby backend-shell alembic upgrade head

../docker-compose.sh exec backend-shell python -m gabby \
  sudo import create-user \
    jacquev6+gabby-dev-admin@gmail.com \
    --username admin \
    --password password

rev_id_arg=
if [ -e ../../backend/gabby/migrations/versions/*_dev.py ]
then
  rev_id_arg="--rev-id $(find ../../backend/gabby/migrations/versions/*_dev.py | sed -E 's#../../backend/gabby/migrations/versions/(.*)_dev\.py#\1#')"
  ../docker-compose.sh exec --workdir /app/backend/gabby backend-shell alembic downgrade head-1
  rm -f ../../backend/gabby/migrations/versions/*_dev.py
fi

../docker-compose.sh exec --workdir /app/backend/gabby backend-shell alembic revision --autogenerate $rev_id_arg -m dev
echo "Check the new revision. Press enter to continue, Ctrl+C to abort."
read

# Check the new revision can be applied and rollbacked
../docker-compose.sh exec --workdir /app/backend/gabby backend-shell alembic upgrade head
../docker-compose.sh exec --workdir /app/backend/gabby backend-shell alembic downgrade head-1

../docker-compose.sh exec --workdir /app/backend/gabby backend-shell alembic upgrade head
../docker-compose.sh exec backend-shell python -m gabby graph-models
