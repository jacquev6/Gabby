#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


gabby_version=$1
test -n "$gabby_version"

push=$2

if $push
then
  args="--platform linux/amd64,linux/arm64 --push"
else
  args="--platform linux/amd64 --load"
fi

docker buildx use gabby-multi-platform-builder 2>/dev/null || docker buildx create --name gabby-multi-platform-builder --use

for part in frontend backend
do
  docker buildx build .. --file $part/Dockerfile \
    --build-arg GABBY_VERSION=$gabby_version \
    --tag jacquev6/gabby-$part:$gabby_version \
    $args
done
