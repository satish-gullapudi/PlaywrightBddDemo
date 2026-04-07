FROM mcr.microsoft.com/playwright/python:v1.50.0-noble

# Update CA certificates to handle SSL handshake properly
RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates

WORKDIR /app

# This layer stays cached unless you change requirements.txt.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install browsers once.
# This layer is now protected. Even if you edit main.py, Docker won't re-download these.
RUN playwright install chromium --with-deps

# Install Java (Required for Allure)
RUN apt-get update && apt-get install -y openjdk-17-jre-headless curl && \
    rm -rf /var/lib/apt/lists/*

# Install Allure Commandline
RUN curl -o allure-2.32.0.tgz -L https://github.com/allure-framework/allure2/releases/download/2.32.0/allure-2.32.0.tgz \
    && tar -zxvf allure-2.32.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.32.0/bin/allure /usr/bin/allure \
    && rm allure-2.32.0.tgz

# Since you edit code often, keep this at the very bottom.
COPY . .

EXPOSE 8501

ENTRYPOINT ["python", "-m", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]