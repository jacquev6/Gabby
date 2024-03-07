#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


if [ -f "../../backend/textbooks/migrations/0002_*.py" ]
then
  echo "Please update the script to keep all but last migration"
  exit 1
fi

docker compose exec backend ./manage.py migrate textbooks zero
rm -f ../../backend/textbooks/migrations/????_*.py
docker compose exec backend ./manage.py makemigrations textbooks
docker compose exec backend ./manage.py migrate textbooks
docker compose exec backend ./manage.py loaddata test-exercises
docker compose exec backend bash -c './manage.py shell <../dev-env/backend/startup.py'
