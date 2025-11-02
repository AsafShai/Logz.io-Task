FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync

COPY src/ ./src/

CMD ["uv", "run", "-m", "src.main"]