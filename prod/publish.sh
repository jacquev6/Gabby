#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."


# Check cleanliness

if [ $(git branch --show-current) != main ]
then
  echo "Not on branch 'main'. Aborting."
  exit 1
fi

if [ "$(git ls-files --others --exclude-standard)" != "" ]
then
  git ls-files --others --exclude-standard
  echo "Untracked files. Aborting."
  exit 1
fi

if ! git diff --stat --exit-code
then
  echo "Unstaged changes. Aborting."
  exit 1
fi

if ! git diff --stat --staged --exit-code
then
  echo "Staged-but-not-committed changes will be included in publication commit. Press enter to continue, Ctrl+C to abort."
  read
fi

# Prepare

gabby_version=$(date +%Y%m%d-%H%M%S)

echo "Edit the changelog for version $gabby_version and press enter to continue, Ctrl+C to abort."
read
git add .
git commit -m "Publish version $gabby_version"

# Build and publish

prod/build.sh $gabby_version push
git tag $gabby_version
git push origin main --tags

# Continue working

git checkout develop
git merge --ff-only main
git push origin develop
