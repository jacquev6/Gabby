#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


docker compose exec new-backend ./manage.py migrate
docker compose exec new-backend ./manage.py migrate textbooks zero
rm -f ../../backend/textbooks/migrations/0002_initial.py
mv ../../backend/textbooks/migrations/0003_initial_patch.py{,_}
docker compose exec new-backend ./manage.py makemigrations textbooks
mv ../../backend/textbooks/migrations/0003_initial_patch.py{_,}
docker compose exec new-backend ./manage.py migrate textbooks
docker compose exec new-backend ./manage.py loaddata test-exercises
docker compose exec new-backend bash -c './manage.py shell <../dev-env/backend/startup.py'
docker compose exec new-backend ./manage.py graph_models textbooks --disable-sort-fields --rankdir BT --output textbooks/models.png
