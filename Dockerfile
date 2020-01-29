FROM python:3.7-alpine

ARG environment=production
ENV WORKDIR /app

WORKDIR ${WORKDIR}
RUN apk add --no-cache --virtual .build-deps build-base gcc musl-dev libffi-dev libressl-dev
RUN pip install poetry && poetry config virtualenvs.create false
COPY . ${WORKDIR}
RUN if [ "${environment}" = "production" ] ; then poetry install --no-dev ; else poetry install ; fi && \
    apk --purge del .build-deps && \
    rm ${WORKDIR}/poetry.lock ${WORKDIR}/pyproject.toml

EXPOSE 80
EXPOSE 443

CMD ["python", "main.py"]
