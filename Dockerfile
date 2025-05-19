FROM python:3.11-slim-buster
WORKDIR /app

COPY setup/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
CMD ["20"]
