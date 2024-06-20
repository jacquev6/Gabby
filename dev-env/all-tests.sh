#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


# @todo Provide backend/type-check.sh
backend/unit-tests.sh --failfast

frontend/type-check.sh
frontend/unit-tests.sh --no-console

./end-to-end-tests.sh --no-console
