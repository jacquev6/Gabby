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
    graphviz `# For 'python -m gabby graph-models'` \
    jq \
    postgresql-client `# For DB backup` \
    poppler-utils  `# For 'pdfunite', to make 'pdf-examples/large.pdf'` \
 && true

ARG USER_ID
ARG GROUP_ID
RUN set -x \
 && groupadd --gid $GROUP_ID gabby \
 && useradd --uid $USER_ID --gid $GROUP_ID --create-home --shell /bin/bash gabby

USER gabby
ENV PATH=$PATH:/home/gabby/.local/bin
