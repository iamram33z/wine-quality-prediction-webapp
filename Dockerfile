# Base image with Python 3.12
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Run the following commands to install the required packages
RUN apt update -y && apt install awscli -y

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip==23.1 && pip install -r requirements.txt --verbose

CMD ["python3", "app.py"]