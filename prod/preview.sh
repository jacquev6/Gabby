#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


secrets_ok=true
echo "# Secrets" > .gitignore
while read template; do
  secret="${template%.secret_template}"
  secret="${secret#./}"
  echo "$secret" >> .gitignore
  if [[ ! -f "$secret" ]]; then
    echo "Please create $secret according to $template"
    secrets_ok=false
  fi
done < <(find . -name '*.secret_template')
$secrets_ok

./build.sh preview load

echo "Gabby prod-preview: build"
docker compose build
echo "Gabby prod-preview: pull"
docker compose pull --ignore-buildable

echo "Gabby prod-preview: start"
docker compose up --no-build --pull never --remove-orphans --detach
docker compose logs --follow || true

echo "Gabby prod-preview: clean-up"
docker compose down --remove-orphans
docker compose rm --stop --volumes --force
