#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


set -x

docker compose exec backend-shell python -m gabby \
  restore-database \
    s3://jacquev6/gabby/prod/backups/gabby-backup-20241014-054206.tar.gz \
    --patch-according-to-settings \
    --yes

docker compose exec --workdir /app/backend/gabby backend-shell alembic upgrade head

docker compose exec backend-shell python -m gabby \
  sudo import create-user \
    jacquev6+gabby-dev-admin@gmail.com \
    --username admin \
    --password password

rev_id_arg=
if [ -e ../../backend/gabby/migrations/versions/*_dev.py ]
then
  rev_id_arg="--rev-id $(find ../../backend/gabby/migrations/versions/*_dev.py | sed -E 's#../../backend/gabby/migrations/versions/(.*)_dev\.py#\1#')"
  docker compose exec --workdir /app/backend/gabby backend-shell alembic downgrade head-1
  rm -f ../../backend/gabby/migrations/versions/*_dev.py
fi

docker compose exec --workdir /app/backend/gabby backend-shell alembic revision --autogenerate $rev_id_arg -m dev
echo "Check the new revision. Press enter to continue, Ctrl+C to abort."
read

# Check the new revision can be applied and rollbacked
docker compose exec --workdir /app/backend/gabby backend-shell alembic upgrade head
docker compose exec --workdir /app/backend/gabby backend-shell alembic downgrade head-1

docker compose exec --workdir /app/backend/gabby backend-shell alembic upgrade head
docker compose exec backend-shell python -m gabby graph-models
