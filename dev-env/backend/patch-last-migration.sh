#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


docker compose exec backend ./manage.py migrate textbooks zero
rm -f ../../backend/textbooks/migrations/0002_initial.py
mv ../../backend/textbooks/migrations/0003_initial_patch.py{,_}
docker compose exec backend ./manage.py makemigrations textbooks
mv ../../backend/textbooks/migrations/0003_initial_patch.py{_,}
docker compose exec backend ./manage.py migrate textbooks
docker compose exec backend ./manage.py loaddata test-exercises
docker compose exec backend bash -c './manage.py shell <../dev-env/backend/startup.py'
docker compose exec backend ./manage.py graph_models textbooks --disable-sort-fields --rankdir BT --output textbooks/models.png
