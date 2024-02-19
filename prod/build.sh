#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


# Check cleanliness
test $(git branch --show-current) == main
git diff --stat --exit-code
git diff --stat --staged --exit-code

# @todo(Project management, soon) Pre-fill changelog and ask to edit; git commit -m "Publish version $tag"

# Build
timestamp=$(date +%Y%m%d-%H%M%S)

git tag $timestamp
docker build .. --file frontend/Dockerfile --build-arg GABBY_VERSION=$timestamp --tag jacquev6/gabby-frontend:$timestamp
docker build .. --file backend/Dockerfile --build-arg GABBY_VERSION=$timestamp --tag jacquev6/gabby-backend:$timestamp

# Publish
git push origin --tags
docker push jacquev6/gabby-frontend:$timestamp
docker push jacquev6/gabby-backend:$timestamp
