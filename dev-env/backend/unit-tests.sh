#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


shuffle=""
if [ $# -eq 0 ]
then
  shuffle=--shuffle
fi

# @todo Understand why we get errors saying the DB is till in use without the '--keepdb' option
docker compose exec backend-shell python -Wa manage.py test --keepdb $shuffle "$@"
docker compose exec backend-shell python -m unittest gabby.{users.tests,pings}
