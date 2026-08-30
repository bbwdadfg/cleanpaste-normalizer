FROM python:3.12-slim
WORKDIR /app
COPY entrypoint.sh /app/entrypoint.sh
COPY app.py /app/app.py
RUN chmod +x /app/entrypoint.sh
LABEL org.opencontainers.image.title="cleanpaste-normalizer" \
      org.opencontainers.image.version="0.2.0" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.url="https://cleanpasteai.com/" \
      org.opencontainers.image.source="https://cleanpasteai.com/"
ENTRYPOINT ["/app/entrypoint.sh"]
