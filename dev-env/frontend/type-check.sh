#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/."


# Ugly workaround to re-type 'console.assert'
# Not doable in 'env.d.ts' because '@types/sha.js/index.d.ts' uses '<reference types="node" />'
# *after* 'env.d.ts' is loaded, overriding the override.
sed -i 's/assert(.*): void/assert(condition: any, message?: string, ...optionalParams: any[]): asserts condition/' ../../frontend/node_modules/@types/node/console.d.ts

# @todo Enable 'false' properties in 'tsconfig.app.json'

docker compose exec \
  frontend-shell \
    npx vue-tsc --build --force

if git \
  --no-pager \
    grep \
      -n \
      -e '<script setup>' \
      -e 'defineProps(' \
      -e 'defineEmits(' \
      -e 'defineModel(' \
      -e ': any$' -e ': any[^/]' \
      -e 'as any$' -e 'as any[^/]' \
      -e '@ts-ignore$' -e '@ts-ignore[^/]' \
      -e '\<Number$' -e '\<Number[^.]' \
      -e '\<String$' -e '\<String[^.]' \
      -e '\<Boolean$' -e '\<Boolean[^.]' \
      -e '\<Symbol$' -e '\<Symbol[^.(]' \
      -e '\<Object$' -e '\<Object[^.]' \
      -- \
      ../../frontend/src/{frontend,adapted}*
then
  false
fi

if git ls-files '../../frontend/*.js' | grep -v -e '\.cy\.js$' -e 'cypress/support' -e 'promise-with-resolvers-polyfill.js'
then
  false
fi
