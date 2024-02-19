#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"



# Check cleanliness
test $(git branch --show-current) == main
git diff --stat --exit-code
git diff --stat --staged --exit-code

# Build
gabby_version=$(date +%Y%m%d-%H%M%S)
./build.sh $gabby_version

# @todo(Project management, soon) Pre-fill changelog and ask to edit; git commit -m "Publish version $tag"

# Publish
git tag $gabby_version
git push origin --tags
docker push jacquev6/gabby-frontend:$gabby_version
docker push jacquev6/gabby-backend:$gabby_version
