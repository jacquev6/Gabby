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

docker compose exec backend python -Wa manage.py test $shuffle "$@"
