#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


./format.sh
./type-check.sh
./unit-tests.sh --failfast
