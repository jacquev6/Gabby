FROM python:3.12

ADD backend/requirements.opinion.txt /tmp/requirements.opinion.txt

RUN --mount=type=cache,target=/root/.cache/pip,sharing=locked \
    set -x \
 && pip3 install \
      -r /tmp/requirements.opinion.txt

ADD backend/requirements.app.txt /tmp/requirements.app.txt

RUN --mount=type=cache,target=/root/.cache/pip,sharing=locked \
    set -x \
 && pip3 install \
      -r /tmp/requirements.app.txt
