FROM python:3.11-slim

RUN pip install poetry

WORKDIR /app/

COPY ./poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false
RUN poetry install --directory /app/

COPY ./app /app/

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload" ]
