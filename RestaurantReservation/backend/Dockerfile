FROM ubuntu:20.04 as base

ENV PYTHONUNBUFFERED=1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y software-properties-common vim build-essential libssl-dev libffi-dev libpq-dev
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get install -y python3.7 python3.7-dev python3.7-venv && ln -sf python3.7 /usr/bin/python
RUN python3.7 -m ensurepip
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache --upgrade pip setuptools && \
    pip3 install --upgrade wheel && \
    pip3 install poetry

RUN poetry config virtualenvs.in-project true && \
    poetry config cache-dir "/api/.cache"
RUN poetry config --list

VOLUME /api
WORKDIR /api

FROM base as develop

COPY pyproject.toml poetry.lock /api/

COPY . /api/
RUN rm -rf /api/.venv

RUN poetry install
SHELL ["/bin/bash", "-c"] 
RUN source .venv/bin/activate

FROM develop as production

RUN rm -rf /api/.venv
RUN poetry install --no-dev
SHELL ["/bin/bash", "-c"] 
RUN source .venv/bin/activate

CMD ["bin/bash"]
