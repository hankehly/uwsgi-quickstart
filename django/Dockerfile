FROM python:3.7.2

WORKDIR /app

COPY . /app

RUN pip install poetry --quiet --no-cache-dir --disable-pip-version-check

# virtualenv creation is already isolated
RUN poetry config settings.virtualenvs.create false

RUN poetry install --no-interaction --no-ansi
