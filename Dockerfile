FROM python:3.6-alpine3.15

LABEL mantainer="Hugo Silva Álvarez <hugofer93@gmail.com>"

    # Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # Poetry
    POETRY_VERSION=1.1.14 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    # Pyenv
    PYENV_ROOT=/opt/pyenv
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV PATH="$PYENV_ROOT/bin:$PATH"

WORKDIR /opt/idcardfield

RUN apk add --no-cache --update gcc linux-headers libc-dev \
    && apk add --no-cache --update bash git make zlib-dev libffi-dev bzip2-dev ncurses-dev readline-dev openssl-dev sqlite-dev xz-dev patch \
    && wget -qO- https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && git clone https://github.com/pyenv/pyenv.git ${PYENV_ROOT} \
    && pyenv install 3.6.1 \
    && pyenv install 3.7.0 \
    && pyenv install 3.8.0 \
    && pyenv install 3.9.0 \
    && pyenv install 3.10.0

COPY . .

RUN poetry install --no-root
