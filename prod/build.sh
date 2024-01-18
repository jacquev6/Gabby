#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


tag=$(date +%Y%m%d-%H%M%S)

docker build .. --file frontend/Dockerfile --build-arg GABBY_VERSION=$tag --tag jacquev6/gabby-frontend:$tag

docker push jacquev6/gabby-frontend:$tag
