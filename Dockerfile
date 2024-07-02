# Use the official Python image.
FROM python:3.8-slim

# Set the working directory.
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app.
COPY . .

# Install Scrapy and other dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Run the spider.
CMD ["scrapy", "crawl", "shl"]