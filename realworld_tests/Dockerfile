# Dockerfile (already set up with Playwright)
FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install Playwright deps and browsers
RUN playwright install --with-deps

# Copy full test repo
COPY . .

# Default: run all tests (can override with docker run args)
CMD ["pytest", "-v"]
