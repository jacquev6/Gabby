#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."


ok=true
while read template
do
  file=${template%.opinion.template}
  if ! [ -f "$file" ]
  then
    echo "Please create '$file' according to '$template'"
    ok=false
  fi
done < <(find . -name '*.opinion.template')
$ok

cd dev-env

. .env

echo "$OPINION_APP_NAME dev-env: start (close with Ctrl+C)"
docker compose up --build --remove-orphans --detach
docker compose logs --follow || true

echo "$OPINION_APP_NAME dev-env: clean-up"
docker compose down --remove-orphans
docker compose rm --stop --volumes --force
