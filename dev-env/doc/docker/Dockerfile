FROM python:3.12

RUN --mount=type=cache,target=/root/.cache/pip,sharing=locked \
    set -x \
 && pip3 install \
      sphinx-autobuild \
      watchfiles \
 && true

RUN mkdir -p /doc
