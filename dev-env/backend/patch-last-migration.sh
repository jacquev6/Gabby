#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


docker compose exec backend-shell ./manage.py migrate textbooks zero

rm -f ../../backend/textbooks/migrations/0007_*.{py,sql}

docker compose exec backend-shell ./manage.py makemigrations
docker compose exec backend-shell ./manage.py migrate
docker compose exec backend-shell ./manage.py loaddata test-exercises more-test-exercises
for app in textbooks
do
  docker compose exec backend-shell ./manage.py graph_models $app --disable-sort-fields --rankdir BT --output $app/models.png
  # for migration in ../../backend/$app/migrations/0*.py
  # do
  #   docker compose exec backend-shell ./manage.py sqlmigrate $app $(basename $migration .py) >${migration%.py}.sql
  # done
done
