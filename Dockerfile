FROM python:3.7-alpine

ENV WORKDIR /app

WORKDIR ${WORKDIR}
RUN apk add --no-cache --virtual .build-deps build-base gcc musl-dev libffi-dev openssl-dev
RUN pip install poetry==1.0.0 && poetry config virtualenvs.create false
COPY . ${WORKDIR}
RUN poetry install --no-dev && \
    apk --purge del .build-deps && \
    rm ${WORKDIR}/poetry.lock ${WORKDIR}/pyproject.toml

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "main:app"]
