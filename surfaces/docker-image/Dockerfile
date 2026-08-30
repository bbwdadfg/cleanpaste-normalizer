FROM python:3.12-slim
WORKDIR /app
COPY app.py /app/app.py
COPY LICENSE /app/LICENSE
COPY README.md /app/README.md
ENV CLEANPASTE_VERSION=0.2.0
LABEL org.opencontainers.image.title="cleanpaste-normalizer" \
      org.opencontainers.image.version="0.2.0" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.url="https://cleanpasteai.com/" \
      org.opencontainers.image.source="https://cleanpasteai.com/"
ENTRYPOINT ["python", "/app/app.py"]
