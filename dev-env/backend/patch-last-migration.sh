#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


docker compose exec backend-shell ./manage.py migrate textbooks zero
docker compose exec --workdir /app/backend/gabby backend-shell alembic downgrade head-1

rm -f ../../backend/textbooks/migrations/0007_*.py
rm -f ../../backend/gabby/migrations/versions/*_dev.py

docker compose exec backend-shell ./manage.py makemigrations
docker compose exec --workdir /app/backend/gabby backend-shell alembic revision --autogenerate -m dev

docker compose exec backend-shell ./manage.py migrate
docker compose exec --workdir /app/backend/gabby backend-shell alembic upgrade head

docker compose exec backend-shell ./manage.py loaddata test-exercises more-test-exercises

docker compose exec backend-shell ./manage.py graph_models textbooks --disable-sort-fields --rankdir BT --output textbooks/models.png
docker compose exec backend-shell python -m gabby graph-models
