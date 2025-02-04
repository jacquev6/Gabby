#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"


console_options="--env ELECTRON_ENABLE_LOGGING=1"
while [ $# -gt 0 ]
do
  case "$1" in
    --no-console)
      console_options=""
      shift
      ;;
    *)
      break
      ;;
  esac
done

if (cd ../..; git grep -n '\.only' -- frontend)
then
  false
fi

../docker-compose.sh exec \
  $console_options \
  frontend-shell \
    npx cypress run \
      --component "$@"

# Cypress puts screenshots in a different place when invoked with --spec. Fix that.
for d in $(find ../../frontend/cypress/screenshots -maxdepth 1 -name 'OldTricolorSection*.cy.*' -or -name 'NewTricolorSection*.cy.*')
do
  mkdir -p ../../frontend/cypress/screenshots/adapted/components
  mv $d ../../frontend/cypress/screenshots/adapted/components
done

for d in $(find ../../frontend/cypress/screenshots/adapted/components -maxdepth 1 -name 'OldTricolorSection*.cy.*' | sort)
do
  stem=${d#../../frontend/cypress/screenshots/adapted/components/Old}
  if [ -d ../../frontend/cypress/screenshots/adapted/components/New$stem ]
  then
    echo "Comparing $stem"
    diff -y -W 2000 \
      <(
        cd ../../frontend/cypress/screenshots/adapted/components/Old$stem
        md5sum *.png \
        | sed \
          -e s/784ec69b0162c249c946149e1de64688/e6aaf11ce2cef3a278a090819c9ff4e3/ \
          -e s/0f99aff1a3fc239e87690788d1f600cd/920adeab85c7700d73f635068e40bfe6/ \
          -e s/784ec69b0162c249c946149e1de64688/e6aaf11ce2cef3a278a090819c9ff4e3/ \
          -e s/b7824e5f29e06f8dff67ca97046c4c41/543adba3e779cb4292918a9c0603a124/ \
          -e s/1f8e5734fab658155e970cfd03d38c36/5400f9f10e254dd3df995e2fc9d386a1/ \
          -e s/12b76e3ac461588951a8872dc1fa032c/5994fe70f8739278903465266286a52c/ \
      ) \
      <(
        cd ../../frontend/cypress/screenshots/adapted/components/New$stem
        md5sum *.png
      ) \
    | (grep -e '|' || true) \
    | {
      result=true
      while read line
      do
        result=false
        old_hash=$(echo $line | cut -d ' ' -f1)
        f=$(echo $line | cut -d ' ' -f2)
        new_hash=$(echo $line | cut -d ' ' -f4)
        echo "$f: -e s/$old_hash/$new_hash/"
        diff-image \
          ../../frontend/cypress/screenshots/adapted/components/Old$stem/$f \
          ../../frontend/cypress/screenshots/adapted/components/New$stem/$f
      done
      $result
    }
  fi
done
