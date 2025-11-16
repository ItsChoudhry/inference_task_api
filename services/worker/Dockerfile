FROM python:3.10-slim

WORKDIR /app

# Update package lists and install curl
RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

RUN uv --version

COPY services/worker /app/services/worker

COPY pyproject.toml .

RUN uv sync

EXPOSE 9000

CMD ["uv", "run", "uvicorn", "services.worker.main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]
