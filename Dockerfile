FROM python:3.7-alpine

ENV WORKDIR /app

WORKDIR ${WORKDIR}
RUN pip install poetry && poetry config settings.virtualenvs.create false
RUN apk add --no-cache --virtual .build-deps build-base gcc musl-dev
COPY . ${WORKDIR}
RUN poetry install --no-dev && \
    apk --purge del .build-deps && \
    rm ${WORKDIR}/poetry.lock ${WORKDIR}/pyproject.toml

CMD ["python", "main.py"]
