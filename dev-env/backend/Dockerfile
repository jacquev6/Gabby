FROM python:3.12-slim

ADD requirements.txt /tmp/requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip,sharing=locked \
    set -x \
 && pip3 install \
      -r /tmp/requirements.txt
