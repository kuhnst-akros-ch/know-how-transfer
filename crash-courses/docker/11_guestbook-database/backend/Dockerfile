FROM python:3-slim

RUN pip install --no-cache-dir flask psycopg2-binary
WORKDIR /app
COPY app.py .
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
