FROM python:3.12

# https://docs.docker.com/engine/reference/builder/#run---mounttypecache
RUN set -x \
 && rm -f /etc/apt/apt.conf.d/docker-clean \
 && echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' >/etc/apt/apt.conf.d/keep-cache

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    set -x \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-recommends \
    graphviz `# For 'manage.py graph_models'` \
    jq \
    postgresql-client `# For DB backup` \
 && true

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
