FROM python:3.12.6-slim AS builder
WORKDIR /build
RUN pip wheel --no-cache-dir --wheel-dir wheels uvicorn
COPY ./requirements.txt .
COPY ./pyproject.toml .
COPY src src
RUN pip wheel --no-cache-dir --wheel-dir wheels .

FROM python:3.12.6-slim AS runner
WORKDIR /app
COPY --from=builder /build/wheels /wheels
RUN pip install --no-cache /wheels/* && rm -rf /wheels
EXPOSE 8000
CMD ["uvicorn", "sentiment_analyser.main:app", "--host", "0.0.0.0", "--port", "8000"]

