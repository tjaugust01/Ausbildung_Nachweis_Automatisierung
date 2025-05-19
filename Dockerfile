FROM python:3.11-slim-buster

WORKDIR /app

# Install necessary packages (locales and poppler-utils), generate locale, and clean up
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    locales \
    poppler-utils && \
    rm -rf /var/lib/apt/lists/* && \
    sed -i -e 's/# de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    locale-gen de_DE.UTF-8

# Set environment variables for the locale
ENV LANG de_DE.UTF-8
ENV LANGUAGE de_DE:de
ENV LC_ALL de_DE.UTF-8

# ... rest of your Dockerfile
COPY setup/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENTRYPOINT ["python", "main.py"]
CMD ["20"]