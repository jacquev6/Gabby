#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


coverage=false
runner="python"
if [ $# -gt 0 ] && [ $1 == --coverage ]
then
  coverage=true
  runner="python -m coverage run --branch"
  shift
fi


defined=$(git grep -e '^    def test' -- ../../backend | wc -l)

imported=$(git grep -e 'from .* import .*ApiTestCase' -- ../../backend/fastjsonapi | wc -l)

inherited=$(git grep -e 'class .*TestCase(.*ApiTestCase)' -- ../../backend/fastjsonapi | wc -l)

expected=$(expr $defined + $imported + $inherited)

echo "Expecting to run $expected tests"

rm -f ../../backend/.coverage
docker compose exec \
  --env GABBY_UNITTESTING=true \
  backend-shell \
    rm -rf /app/dev-env/backend/unit-tests-coverage

docker compose exec \
  --env GABBY_UNITTESTING=true \
  backend-shell \
    $runner -m unittest discover --pattern '*.py' "$@"

if $coverage
then
  docker compose exec \
    --env GABBY_UNITTESTING=true \
    backend-shell \
      python -m coverage html --quiet --dir /app/dev-env/backend/unit-tests-coverage
fi

rm -f ../../backend/.coverage
