#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


rev_id_arg=
if [ -e ../../backend/gabby/migrations/versions/*_dev.py ]
then
  rev_id_arg="--rev-id $(find ../../backend/gabby/migrations/versions/*_dev.py | sed -E 's#../../backend/gabby/migrations/versions/(.*)_dev\.py#\1#')"
  docker compose exec --workdir /app/backend/gabby backend-shell alembic downgrade head-1
  rm -f ../../backend/gabby/migrations/versions/*_dev.py
else
  docker compose exec --workdir /app/backend/gabby backend-shell alembic upgrade head
fi

docker compose exec --workdir /app/backend/gabby backend-shell alembic revision --autogenerate $rev_id_arg -m dev

docker compose exec --workdir /app/backend/gabby backend-shell alembic upgrade head
docker compose exec backend-shell python -m gabby graph-models
