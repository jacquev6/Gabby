#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


# @todo Do this in a Docker container (for repeatability)
pdfunite $(for n in $(seq 32); do echo test.pdf; done) large.pdf
