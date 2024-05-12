#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


docker compose exec backend-shell ./manage.py migrate textbooks zero
docker compose exec backend-shell ./manage.py migrate opinion_ping zero

rm -f ../../backend/textbooks/migrations/0006_*.{py,sql}
rm -f ../../backend/opinion_ping/migrations/0004_*.{py,sql}

docker compose exec backend-shell ./manage.py makemigrations
docker compose exec backend-shell ./manage.py migrate
docker compose exec backend-shell ./manage.py loaddata test-users test-exercises more-test-exercises
for app in textbooks opinion_ping
do
  docker compose exec backend-shell ./manage.py graph_models $app --disable-sort-fields --rankdir BT --output $app/models.png
  # for migration in ../../backend/$app/migrations/0*.py
  # do
  #   docker compose exec backend-shell ./manage.py sqlmigrate $app $(basename $migration .py) >${migration%.py}.sql
  # done
done
