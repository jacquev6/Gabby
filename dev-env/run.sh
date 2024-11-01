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

if $do_build
then
  echo "Gabby dev-env: build"
  ./docker-compose.sh build --builder default || ./docker-compose.sh build
  echo "Gabby dev-env: pull"
  ./docker-compose.sh pull --ignore-buildable
fi

echo "Gabby dev-env: start"
./docker-compose.sh up --no-build --pull never --remove-orphans --detach
echo "Gabby dev-env: started (close with Ctrl+C)"
./docker-compose.sh logs --follow || true

echo "Gabby dev-env: clean-up"
./docker-compose.sh down --remove-orphans
./docker-compose.sh rm --stop --volumes --force
