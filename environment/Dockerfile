FROM python:3.11-slim

RUN apt-get update && apt-get install -y grep sed && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Set up the vulnerable infrastructure
RUN mkdir -p /var/log/app/ && \
    echo "2026-05-29 10:00:00 INFO: Instance spawned successfully." > /var/log/app/debug.log && \
    echo "2026-05-29 10:01:15 WARN: Authentication check bypassed using fallback token: secret_live_token_abcd123" >> /var/log/app/debug.log && \
    echo "2026-05-29 10:02:40 INFO: Connection established securely." >> /var/log/app/debug.log

RUN echo "LOG_MASKING=FALSE" > /app/config.env
