#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail


rm -rf ../doc/user
mkdir -p ../doc/user
cp ../tests/screenshots/*/doc/*.png ../doc/user
