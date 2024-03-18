#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


docker compose exec \
  frontend \
    cp node_modules/pdfjs-dist/build/pdf.worker.min.mjs public/pdf.worker.min.js
