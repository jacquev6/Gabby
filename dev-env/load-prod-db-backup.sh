#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


./docker-compose.sh exec \
  backend-shell python -m gabby \
    restore-database \
      s3://jacquev6/gabby/prod/backups/gabby-backup-20241112-144747.tar.gz \
      --patch-according-to-settings \
      --yes
