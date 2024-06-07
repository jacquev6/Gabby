#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


defined=$(git grep -e '^    def test' -- ../../backend | wc -l)

imported=$(git grep -e 'from .* import .*ApiTestCase' -- ../../backend | wc -l)

inherited=$(git grep -e 'class .*TestCase(.*ApiTestCase)' -- ../../backend | wc -l)

expected=$(expr $defined + $imported + $inherited)

echo "Expecting to run $expected tests"

docker compose exec --env GABBY_UNITTESTING=true backend-shell python -m unittest discover --pattern '*.py' "$@"
