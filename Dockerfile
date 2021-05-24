FROM alpine:3.7
RUN apk add --no-cache --update \
    bash \
    build-base \
    curl \
    git \
    libffi-dev \
    openssl-dev \
    make

ENV PYTHONUNBUFFERED=1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN apk add --no-cache --update python3.7 python3.7-dev && ln -sf python3.7 /usr/bin/python
RUN python3.7 -m ensurepip
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache --upgrade pip setuptools && \
    pip3 install --upgrade wheel && \
    pip3 install poetry

RUN poetry config virtualenvs.in-project true && \
    poetry config cache-dir "/project/.cache"
RUN poetry config --list

COPY pyproject.toml poetry.lock /project/

COPY . /project/
RUN rm -rf /project/.venv

RUN /root/.poetry/bin/poetry install

WORKDIR /project
RUN rm -rf /project/.venv
RUN /root/.poetry/bin/poetry install --no-dev
RUN source .venv/bin/activate

CMD ["bin/bash"]
