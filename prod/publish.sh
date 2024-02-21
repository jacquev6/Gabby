#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"



# Check cleanliness
test $(git branch --show-current) == main
git diff --stat --exit-code
git diff --stat --staged --exit-code

gabby_version=$(date +%Y%m%d-%H%M%S)

echo "Edit the changelog for version $gabby_version and press enter to continue"
read
git add .
git commit -m "Publish version $gabby_version"

# Build and publish
./build.sh $gabby_version true
git tag $gabby_version
git push origin main --tags
