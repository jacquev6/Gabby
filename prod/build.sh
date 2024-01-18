#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


# Check cleanliness
git diff --stat --exit-code
git diff --stat --staged --exit-code

# Build
timestamp=$(date +%Y%m%d-%H%M%S)

git tag $timestamp
docker build .. --file frontend/Dockerfile --build-arg GABBY_VERSION=$timestamp --tag jacquev6/gabby-frontend:$timestamp

# Publish
git push origin --tags
docker push jacquev6/gabby-frontend:$timestamp
