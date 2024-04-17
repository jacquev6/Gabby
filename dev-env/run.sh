#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."


do_build=true
while [ $# -gt 0 ]
do
  case "$1" in
    --no-build)
      do_build=false
      ;;
    *)
      echo "Unknown argument: $1"
      exit 1
      ;;
  esac
  shift
done

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

if $do_build
then
  echo "$OPINION_APP_NAME dev-env: build"
  docker compose build --builder default || docker compose build
  echo "$OPINION_APP_NAME dev-env: pull"
  docker compose pull --ignore-buildable
fi

echo "$OPINION_APP_NAME dev-env: start"
docker compose up --no-build --pull never --remove-orphans --detach
echo "$OPINION_APP_NAME dev-env: started (close with Ctrl+C)"
docker compose logs --follow || true

echo "$OPINION_APP_NAME dev-env: clean-up"
docker compose down --remove-orphans
docker compose rm --stop --volumes --force
