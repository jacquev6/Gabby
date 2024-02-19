#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


gabby_version=$1
test -n "$gabby_version"

docker build .. --file frontend/Dockerfile --build-arg GABBY_VERSION=$gabby_version --tag jacquev6/gabby-frontend:$gabby_version
docker build .. --file backend/Dockerfile --build-arg GABBY_VERSION=$gabby_version --tag jacquev6/gabby-backend:$gabby_version
