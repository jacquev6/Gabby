#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


./shell.sh -c 'python -Wa manage.py test --shuffle'
