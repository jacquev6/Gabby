#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


docker compose exec \
  frontend \
    npx cypress run \
      --component


# @todo Ensure that templates have no untranslated content
# @body Ensure that no data-bs-* attributes are used
