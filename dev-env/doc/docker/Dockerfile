FROM python:3.12

ARG USER_ID
ARG GROUP_ID
RUN set -x \
 && groupadd --gid $GROUP_ID gabby \
 && useradd --uid $USER_ID --gid $GROUP_ID --create-home --shell /bin/bash gabby

USER gabby
ENV PATH=$PATH:/home/gabby/.local/bin

RUN --mount=type=cache,target=/home/gabby/.cache/pip,sharing=locked \
    set -x \
 && pip3 install \
      sphinx-autobuild \
      watchfiles \
 && true

 RUN mkdir -p /home/gabby/doc
