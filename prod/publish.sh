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

# Build and publish
gabby_version=$(date +%Y%m%d-%H%M%S)
./build.sh $gabby_version true
git tag $gabby_version
git push origin --tags
