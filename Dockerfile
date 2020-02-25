FROM python:3.7-slim

ENV WORKDIR /app

WORKDIR ${WORKDIR}
RUN pip install poetry==0.12.17 && poetry config settings.virtualenvs.create false
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc-dev

COPY . ${WORKDIR}

RUN poetry install --no-dev \
    && apt-get purge -y --auto-remove gcc libc-dev

CMD ["python", "main.py"]
